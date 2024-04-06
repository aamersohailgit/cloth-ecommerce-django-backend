from django.db import models
from django.contrib import admin
from django.urls import reverse


# Create category model for e-commerce
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="photos/categories", blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse("products_by_category", args=[self.slug])

    def get_absolute_url(self):
        return reverse("products_by_category", args=[self.slug])
