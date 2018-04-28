from rest_framework import permissions, generics, filters
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

from api.backends import AnonymousUserAuthentication, AuthentiaUserTokenAuthentication, CompanyUserTokenAuthentication


class RequireAuthenticationMixin(object):
    permission_classes = (permissions.IsAuthenticated,)


class RequireAnyTokenMixin(RequireAuthenticationMixin):
    authentication_classes = (AuthentiaUserTokenAuthentication, CompanyUserTokenAuthentication,
        SessionAuthentication, BasicAuthentication, AnonymousUserAuthentication)
