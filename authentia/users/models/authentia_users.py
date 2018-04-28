from django.contrib.gis.db import models
from django.core import signing

from users.models import AuthentiaAbstractBaseUser, TokenUserModel


class AuthentiaUser(AuthentiaAbstractBaseUser):
    token = models.OneToOneField(TokenUserModel, related_name="user_token", null=True, blank=True, on_delete=models.CASCADE, max_length=250)

    def generate_sign(self):
        return signing.dumps(self.pk)

    def __str__(self):
        return "{} {} {}".format(self.pk, self.full_name, self.token)
