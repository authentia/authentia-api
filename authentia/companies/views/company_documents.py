from rest_framework import generics

from companies.models import CompanyDocument
from api.serializers.company_documents import CompanyDocumentSerializer
from api.helpers.views import RequireAnyTokenMixin


class CompanyDocumentListCreateView(RequireAnyTokenMixin, generics.ListCreateAPIView):
    """
    """
    queryset = CompanyDocument.objects.all()
    serializer_class = CompanyDocumentSerializer

    def get_queryset(self):
        company = self.request.user.company
        return self.queryset.filter(company=company)


class CompanyDocumentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = CompanyDocument.objects.all()
    serializer_class = CompanyDocumentSerializer
