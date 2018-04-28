from rest_framework import generics

from users.models import UserDocument
from api.serializers.user_documents import UserDocumentSerializer, RequireAnyTokenMixin


class UserDocumentListCreateView(RequireAnyTokenMixin, generics.ListCreateAPIView):
    """
    """
    queryset = UserDocument.objects.all()
    serializer_class = UserDocumentSerializer


class UserDocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = UserDocument.objects.all()
    serializer_class = UserDocumentSerializer
