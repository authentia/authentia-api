from django.db import models

from base.models import BaseModel
from helpers import upload_to_kwargs, upload_to_generic


class Transaction(BaseModel):
    STATUS_CHOICES = (
        (0, 'not verified'),
        (1, 'verified'),
    )

    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    user = models.ForeignKey('users.AuthentiaUser', on_delete=models.CASCADE)
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=0)
    photo = models.ImageField(upload_to=upload_to_kwargs(upload_to_generic, subfolder="transaction-photo"))

    def __str__(self):
        return self.pk
