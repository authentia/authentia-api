from rest_framework import serializers

from base.models import DocumentType


class DocumentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocumentType
        exclude = ('created', )
