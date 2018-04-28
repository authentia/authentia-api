from django.contrib.gis.db import models
from django.core import signing

from users.models import AuthentiaAbstractBaseUser, TokenUserModel


class CompanyUser(AuthentiaAbstractBaseUser):
    company = models.OneToOneField('companies.Company', on_delete=models.CASCADE, null=True, blank=True)
    token = models.OneToOneField(TokenUserModel, related_name="company_user_token", null=True, blank=True, on_delete=models.CASCADE, max_length=250)

    def generate_sign(self):
        return signing.dumps(self.pk)

    def __str__(self):
        return "{} {} {}".format(self.pk, self.full_name, self.token)
