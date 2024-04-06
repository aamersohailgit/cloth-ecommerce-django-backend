from django.db import models
from store.models import ProductModel, VariationModel
from core.settings import AUTH_USER_MODEL


class CartModel(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

    # verbose
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


# Create CartItemModel
class CartItemModel(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    variations = models.ManyToManyField(VariationModel, blank=True)
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product

    # verbose
    class Meta:
        verbose_name_plural = "Cart Items"
