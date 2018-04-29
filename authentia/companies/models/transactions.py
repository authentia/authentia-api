from django.db import models

from base.models import BaseModel


class Transaction(BaseModel):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    user = models.ForeignKey('base.DocumentType', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.company.name, self.user.first_name)
