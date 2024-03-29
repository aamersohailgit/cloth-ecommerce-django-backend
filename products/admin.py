from django.contrib import admin
from products.models import ProductModel, StateModel

admin.site.register(StateModel)
admin.site.register(ProductModel)
