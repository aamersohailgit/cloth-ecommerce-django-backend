import razorpay
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import OrderModel, PaymentModel
from django.utils import timezone

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))


@api_view(["POST"])
def create_order(request):
    data = request.data
    payment = client.order.create(dict(amount=data["amount"], currency="INR"))
    order = OrderModel.objects.create(
        razorpay_order_id=payment["id"],
        entity=payment["entity"],
        amount=payment["amount"],
        amount_paid=payment["amount_paid"],
        amount_due=payment["amount_due"],
        currency=payment["currency"],
        receipt=payment["receipt"],
        offer_id=payment["offer_id"],
        status=payment["status"],
        attempts=payment["attempts"],
        notes=payment.get("notes"),
    )
    return Response(payment, status=status.HTTP_200_OK)


@api_view(["POST"])
def payment_success(request):
    # Extract payment details from request
    razorpay_order_id = request.data.get("razorpay_order_id")
    razorpay_payment_id = request.data.get("razorpay_payment_id")
    razorpay_signature = request.data.get("razorpay_signature")

    # Logic to verify payment signature
    params_dict = {
        "razorpay_order_id": razorpay_order_id,
        "razorpay_payment_id": razorpay_payment_id,
        "razorpay_signature": razorpay_signature,
    }

    try:
        # Verify the payment signature
        client.utility.verify_payment_signature(params_dict)
        # If signature is verified, update the order status
        order = OrderModel.objects.get(razorpay_order_id=razorpay_order_id)
        order.status = "paid"
        order.save()

        PaymentModel.objects.create(
            order=order,
            razorpay_payment_id=razorpay_payment_id,
            razorpay_signature=razorpay_signature,
            payment_method="razorpay",
        )

        # Then, return a success response
        return Response({"status": "Payment successful"}, status=status.HTTP_200_OK)
    except razorpay.errors.SignatureVerificationError:
        return Response(
            {"error": "Invalid payment signature"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except OrderModel.DoesNotExist:
        return Response(
            {"error": "Order does not exist"}, status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return Response(
            {"error": "Something went wrong", "message": str(e)},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def payment_failure(request):
    print("Payment failed-----_")
    print(request.data)
    data = request.data
    razorpay_order_id = data.get("razorpay_order_id", None)
    try:
        order = OrderModel.objects.get(razorpay_order_id=razorpay_order_id)
        order.status = "failed"
        order.updated_at = timezone.now()
        order.save()
        return Response({"status": "Payment failed"}, status=status.HTTP_200_OK)
    except OrderModel.DoesNotExist:
        return Response(
            {"error": "Order does not exist"}, status=status.HTTP_400_BAD_REQUEST
        )