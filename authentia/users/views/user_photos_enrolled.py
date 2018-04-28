from rest_framework import generics

from users.models import PhotoEnroll
from api.serializers.user_documents import PhotoEnrollSerializer
from api.helpers.views import RequireAnyTokenMixin


class PhotoEnrollListCreateView(RequireAnyTokenMixin, generics.ListCreateAPIView):
    """
    """
    queryset = PhotoEnroll.objects.all()
    serializer_class = PhotoEnrollSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)


class PhotoEnrollRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = PhotoEnroll.objects.all()
    serializer_class = PhotoEnrollSerializer
