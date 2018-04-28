from django.db import models


class BaseModel(models.Model):
    """An abstract base class model that provides self-updating `created` and
    `modified` fields, along with some methods for uniquely identifying instances.
    """
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created']


class DocumentType(BaseModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
