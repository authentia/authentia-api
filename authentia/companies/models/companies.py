from django.db import models

from base.models import BaseModel


class Company(BaseModel):
    bussiness_name = models.CharField(max_length=64)
    tax_id = models.CharField(max_length=64)
    email_contact = models.CharField(max_length=64)
    phone_contact = models.CharField(max_length=64)
    legal_respresentative = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.bussiness_name
