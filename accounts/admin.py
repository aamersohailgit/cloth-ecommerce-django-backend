from django.contrib import admin
from accounts.models import AccountModel, UserAddressModel, UserProfileModel
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from accounts.models import RoleModel

class RoleAdmin(admin.ModelAdmin):
    list_display = ("id","name", "description")
    search_fields = ("name", "description")
    

admin.site.register(RoleModel, RoleAdmin)


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "date_joined",
        "last_login",
        "is_admin",
        "is_staff",
    )

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {"fields": ("first_name", "last_name", "username", "phone_number")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = (
        "email",
        "id",
        "first_name",
        "last_name",
        "username",
        "phone_number",
        "is_active",
        "is_staff",
        "is_admin",
    )
    search_fields = ("first_name", "last_name", "email")
    ordering = ("email",)
    readonly_fields = ["date_joined", "last_login"]


class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "address_line_1",
        "address_line_2",
        "city",
        "state",
        "zipcode",
        "country",
    )
    list_filter = ("user", "city", "state", "country")
    search_fields = ("user", "city", "state", "country")


# create UserProfileAdmin class
class UserProfileModelAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return mark_safe(
            '<img src="{}" width="40" style="border-radius: 50%;" />'.format(
                object.profile_picture.url
            )
        )

    thumbnail.short_description = "Profile Picture"
    list_display = (
        "thumbnail",
        "user",
        "city",
        "state",
        "country",
        "zipcode",
        "address_line_1",
        "address_line_2",
    )
    list_filter = ("user", "city", "state", "country")
    search_fields = ("user", "city", "state", "country", "zipcode")
    # readonly_fields = ("date_joined", "last_login")


# Register your models here.
admin.site.register(AccountModel, AccountAdmin)
admin.site.register(UserAddressModel, AddressAdmin)
admin.site.register(UserProfileModel, UserProfileModelAdmin)
