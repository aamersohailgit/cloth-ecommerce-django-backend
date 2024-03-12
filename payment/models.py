from django.db import models
from django.utils import timezone
import uuid


class OrderModel(models.Model):
    STATUS_CHOICES = [
        ("created", "Created"),
        ("paid", "Paid"),
        ("failed", "Failed"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity = models.CharField(max_length=50, default="order")
    razorpay_order_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default="INR")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="created")
    receipt = models.CharField(max_length=50, null=True, blank=True)
    offer_id = models.CharField(max_length=50, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.razorpay_order_id
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class PaymentModel(models.Model):
    order = models.ForeignKey(
        OrderModel, on_delete=models.CASCADE, related_name="payments"
    )
    razorpay_payment_id = models.CharField(max_length=50, unique=True)
    razorpay_signature = models.CharField(max_length=255)
    payment_method = models.CharField(
        max_length=50, null=True, blank=True
    )  # Assuming you might want to store this
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razorpay_payment_id
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
