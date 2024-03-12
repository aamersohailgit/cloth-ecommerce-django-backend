from django.urls import path
from .views import create_order, payment_success, payment_failure

urlpatterns = [
    path("create_order/", create_order, name="create_order"),
    path("payment_success/", payment_success, name="payment_success"),
    path("payment_failure/", payment_failure, name="payment_failure"),
]
