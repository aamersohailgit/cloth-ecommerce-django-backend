from django.contrib import admin
from .models import OrderModel, PaymentModel

class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'razorpay_order_id', 'amount', 'status', 'created_at', 'updated_at']

class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['order', 'razorpay_payment_id', 'payment_method', 'created_at']

admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(PaymentModel, PaymentModelAdmin)