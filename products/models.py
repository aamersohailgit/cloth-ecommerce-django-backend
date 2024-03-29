from django.db import models
from django.urls import reverse


class StateModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "state"
        verbose_name_plural = "states"


class ProductModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to="photos/products")
    location = models.CharField(max_length=50, blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    states = models.ManyToManyField(StateModel, blank=True, related_name="products")
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        help_text="Percentage discount if applicable",
    )

    def get_url(self):
        # Ensure the category relationship or logic here is correctly implemented
        return reverse("product_detail", args=[self.category.slug, self.slug])

    def final_price(self):
        """Calculate final price after discount, if applicable."""
        if self.discount > 0:
            return self.price - (self.price * self.discount / 100)
        return self.price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
