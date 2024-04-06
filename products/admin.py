from django.contrib import admin
from products.models import ProductGalleryModel, ProductModel


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "stock", "is_available", "created_date"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ProductGalleryModel)
