from django.contrib.gis.db import models
from django.core import signing

from users.models import AuthentiaAbstractBaseUser, TokenUserModel
from base.models import BaseModel
from helpers import upload_to_kwargs, upload_to_generic


class AuthentiaUser(AuthentiaAbstractBaseUser):
    token = models.OneToOneField(TokenUserModel, related_name="user_token", null=True, blank=True, on_delete=models.CASCADE, max_length=250)

    def generate_sign(self):
        return signing.dumps(self.pk)

    def __str__(self):
        return "{} {} {}".format(self.pk, self.full_name, self.token)


class PhotoEnroll(BaseModel):
    user = models.ForeignKey(AuthentiaUser, on_delete=models.CASCADE)
    file = models.ImageField(upload_to=upload_to_kwargs(upload_to_generic, subfolder="photos-enrolled"))

    # def save(self):
    #     enroll with api
    #     pass

    def __str__(self):
        return self.user.first_name
