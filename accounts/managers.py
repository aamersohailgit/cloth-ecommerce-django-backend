from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    def email_validation(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("You must provide a valid email address")

    def create_user(
        self, username, email, first_name, last_name=None, password=None, **extra_fields
    ):
        if not email:
            raise ValueError("Users must have an email address")
        else:
            self.email_validation(email)
            clean_email = self.normalize_email(email)
        if not first_name:
            raise ValueError("Users must have a first name")

        user = self.model(
            email=clean_email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)

        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, email, first_name, last_name=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_active", True)

        if not email:
            raise ValueError(_("This is required field"))
        else:
            self.email_validation(email)
            clean_email = self.normalize_email(email)
        if not first_name:
            raise ValueError(_("This is required field"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have True value in is_superuser field"))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have True value in is_staff field"))

        user = self.create_user(
            username, clean_email, first_name, last_name, password, **extra_fields
        )

        user.save(using=self._db)

        return user
