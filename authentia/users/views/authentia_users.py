from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import AuthentiaUser, TokenUserModel
from api.serializers.authentia_users import AuthentiaUserSerializer
from api.serializers.users import UserAuthTokenSerializer


class AuthentiaUserAuthView(APIView):
    """
    """

    serializer_class = UserAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        credentials = self.serializer_class(data=request.data)
        credentials.is_valid(raise_exception=True)
        authentia = credentials.validated_data['user']
        token, created = TokenUserModel.objects.get_or_create(user_token=authentia)
        token.save()
        authentia.token = token
        authentia.save()
        return Response({'token': token.key, 'user_id': authentia.pk, 'user_email': authentia.email, 'user_name': authentia.get_short_name })


class AuthentiaListCreateView(generics.ListCreateAPIView):
    """
    """
    queryset = AuthentiaUser.objects.all()
    serializer_class = AuthentiaUserSerializer


class AuthentiaUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    """
    queryset = AuthentiaUser.objects.all()
    serializer_class = AuthentiaUserSerializer
