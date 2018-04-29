from rest_framework import generics
from rest_framework.views import APIView

from users.models import Lead
from api.serializers.leads import LeadSerializer


class LeadListCreateView(generics.ListCreateAPIView):
    """
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


class LeadRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
