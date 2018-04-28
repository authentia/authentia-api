from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import CompanyUser, TokenUserModel
from api.serializers.company_users import CompanyUserSerializer
from api.serializers.users import UserAuthTokenSerializer


class CompanyUserAuthView(APIView):
    """
    """

    serializer_class = UserAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        credentials = self.serializer_class(data=request.data)
        credentials.is_valid(raise_exception=True)
        company_user = credentials.validated_data['user']
        token, created = TokenUserModel.objects.get_or_create(company_user_token=company_user)
        token.save()
        company_user.token = token
        company_user.save()
        return Response({'token': token.key, 'user_id': company_user.pk, 'user_email': company_user.email, 'user_name': company_user.get_short_name })


class CompanyUserListCreateView(generics.ListCreateAPIView):
    """
    """
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer


class CompanyUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = CompanyUser.objects.all()
    serializer_class = CompanyUserSerializer
