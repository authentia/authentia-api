from rest_framework import generics

from companies.models import Company
from api.serializers.companies import CompanySerializer
from api.helpers.views import RequireAnyTokenMixin


class CompanyListCreateView(RequireAnyTokenMixin, generics.ListCreateAPIView):
    """
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(companyuser=user)


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
