import binascii
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from users.manager import AuthentiaUserManager
from base.models import BaseModel


class TokenUserModel(BaseModel):
    """
    The default authorization token model
    """
    key = models.TextField(primary_key=True)

    # def save(self, *args, **kwargs):
    #     if not self.key:
    #         self.key = self.generate_key()
    #     return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def save(self, *args, **kwargs):
        self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.key


class AuthentiaBaseUser(AbstractBaseUser, PermissionsMixin):
    """
    Enables the use of Django's built-in permissions and groups system;
    useful when we have N different user types inheriting from this class.
    This model is created in the database.
    """
    def __str__(self):
        return "{}".format(self.pk)


class AuthentiaAbstractBaseUser(BaseModel, AuthentiaBaseUser):
    """
    Defines common attributes among Authentia User Types
    """
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_admin = models.BooleanField(default=False)

    objects = AuthentiaUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', ]

    class Meta:
        # This model should not be created in the database
        abstract = True

    @property
    def is_staff(self):
        """Returns if the user can access to Django Admin site"""
        return self.is_admin

    @property
    def full_name(self):
        """Concatenate first and last names, trim extra whitespace."""
        name = "{first_name} {last_name}".format(
            first_name=self.first_name,
            last_name=self.last_name,
        )
        return ' '.join(part.capitalize() for part in name.split())

    @property
    def get_short_name(self):
        """First name and initial of last name."""
        name = "{first_name} {last_name}.".format(
            first_name=self.first_name,
            last_name=self.last_name.strip()[:1],
        )
        return ' '.join(part.capitalize() for part in name.split())

    def __str__(self):
        return "{}".format(self.pk)


class AuthentiaDefaultUser(AuthentiaAbstractBaseUser):
    """
    Generic User Type - The one used in AUTH_USER_MODEL for Django Settings
    """
    token = models.OneToOneField(TokenUserModel, related_name="admin_token", null=True, on_delete=models.CASCADE, max_length=250)

    @property
    def is_staff(self):
        """Staff users always can use Django Admin Site"""
        return True
