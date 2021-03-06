from django.db import models

from base.models import BaseModel
from helpers import upload_to_kwargs, upload_to_generic


class CompanyDocument(BaseModel):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    document_type = models.ForeignKey('base.DocumentType', on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_to_kwargs(upload_to_generic, subfolder="company-documents"))

    def __str__(self):
        return self.document_type.name
