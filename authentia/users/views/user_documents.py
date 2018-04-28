from rest_framework import generics

from users.models import UserDocument
from api.serializers.user_documents import UserDocumentSerializer
from api.helpers.views import RequireAnyTokenMixin


class UserDocumentListCreateView(RequireAnyTokenMixin, generics.ListCreateAPIView):
    """
    """
    queryset = UserDocument.objects.all()
    serializer_class = UserDocumentSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class UserDocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = UserDocument.objects.all()
    serializer_class = UserDocumentSerializer
