from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import signing

from companies.models import Company, Transaction
from api.serializers.companies import CompanySerializer
from api.helpers.views import RequireAnyTokenMixin
from api.serializers.users import UserRecognitionSerializer


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



class UserVerificationView(RequireAnyTokenMixin, APIView):
    """
    """

    serializer_class = UserRecognitionSerializer

    def post(self, request, token, *args, **kwargs):
        company = Company.objects.get(pk=signing.loads(token))
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data.get('file')
        transaction = Transaction.objects.create(user=self.request.user, company=company, photo=file)
        verify = self.request.user.verify_user(self.request.build_absolute_uri(transaction.photo.url))
        if verify.get('Errors'):
            return Response({ 'verified': False, 'message': verify.get('Errors')[0].get('Message')})
        elif verify.get('images')[0].get('transaction').get('confidence') < 0.80:
            return Response({ 'verified': False, 'message': 'Not recognized' })
        transaction.status = 1
        transaction.save()
        return Response({'verified': True, 'message': ''})

