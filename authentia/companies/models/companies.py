from django.db import models

from base.models import BaseModel
from django.core import signing


class Company(BaseModel):
    bussiness_name = models.CharField(max_length=64)
    tax_id = models.CharField(max_length=64)
    email_contact = models.EmailField(max_length=64)
    phone_contact = models.CharField(max_length=64)
    legal_respresentative = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    success_url = models.CharField(max_length=64)
    error_url = models.CharField(max_length=64)
    sign = models.CharField(max_length=300, default='')

    def generate_sign(self):
        return signing.dumps(self.pk)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.sign = self.generate_sign()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.bussiness_name
