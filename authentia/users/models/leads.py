from django.contrib.gis.db import models

from base.models import BaseModel


class Lead(BaseModel):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return "{} {} {}".format(self.pk, self.name, self.email)
