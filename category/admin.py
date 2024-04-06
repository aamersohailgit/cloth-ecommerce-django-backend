from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


# Register your Category model
admin.site.register(Category, CategoryAdmin)
