from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import AccountManager
from django.contrib.auth.models import Permission, Group

class RoleModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

        
# add AccountModel class
class AccountModel(AbstractBaseUser):
    objects = AccountManager()

    # create first_name, last_name, email, username, phone number
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    # create required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # create login fields
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    # define verbose
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"


# create UserProfileModel
# create user profile models
class UserProfileModel(models.Model):
    user = models.OneToOneField(AccountModel, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="userprofile", blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.fullname()

    def full_address(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.state}, {self.zipcode}, {self.country}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


# create user address model
class UserAddressModel(models.Model):
    user = models.ForeignKey(AccountModel, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.user.fullname()

    def full_address(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.state}, {self.zipcode}, {self.country}"

    class Meta:
        verbose_name = "User Address"
        verbose_name_plural = "User Addresses"
