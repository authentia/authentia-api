from rest_framework import generics
from rest_framework.views import APIView

from base.models import DocumentType
from api.serializers.document_types import DocumentTypeSerializer


class DocumentTypeListCreateView(generics.ListCreateAPIView):
    """
    """
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class DocumentTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer
