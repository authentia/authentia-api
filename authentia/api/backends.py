from rest_framework import authentication
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.backends import ModelBackend

from users.models import TokenUserModel, AuthentiaUser, CompanyUser

from annoying.functions import get_object_or_None


class AnonymousUserAuthentication(authentication.BaseAuthentication):
    """
    AirMatchDefaultUser authentication by token
    """
    def authenticate(self, request):
        return (AnonymousUser(), 'AnonymousUser')


class AuthentiaUserTokenAuthentication(authentication.BaseAuthentication):
    """
    WoofmeUser authentication by token
    """
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION') # get auth token from header
        if not token:
            return None
        # token_validation(request, 'WoofmeUser')
        try:
            tkn = TokenUserModel.objects.get(key=token)
            try:
                return (tkn.user_token, 'AuthentiaUser')
            except:
                return None
        except TokenUserModel.DoesNotExist:
            return None



class AuthentiaUserBackend(ModelBackend):
    """
    Authenticates agains clients.AuthentiaUser
    This user class is based on default Django User System
    so we can use all has_perms and all perms related functions
    of default ModelBackend and only replace what we need.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        user = get_object_or_None(AuthentiaUser, email=username)

        if not user or not user.check_password(password):
            return None

        return user

    def get_user(self, user_pk):
        """Returns AuthentiaUser based on their Pk"""
        return get_object_or_None(AuthentiaUser, pk=user_pk)


class CompanyUserTokenAuthentication(authentication.BaseAuthentication):
    """
    WoofmeUser authentication by token
    """
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION') # get auth token from header
        if not token:
            return None
        # token_validation(request, 'WoofmeUser')
        try:
            tkn = TokenUserModel.objects.get(key=token)
            try:
                return (tkn.company_user_token, 'CompanyUser')
            except:
                return None
        except TokenUserModel.DoesNotExist:
            return None


class CompanyUserBackend(ModelBackend):
    """
    Authenticates agains clients.CompanyUser
    This user class is based on default Django User System
    so we can use all has_perms and all perms related functions
    of default ModelBackend and only replace what we need.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        user = get_object_or_None(CompanyUser, email=username)

        if not user or not user.check_password(password):
            return None

        return user

    def get_user(self, user_pk):
        """Returns CompanyUser based on their Pk"""
        return get_object_or_None(CompanyUser, pk=user_pk)
