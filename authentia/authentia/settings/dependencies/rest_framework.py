REST_FRAMEWORK = {
    # allow client to override using `?page_size={num}` in query string
    'DEFAULT_PAGINATION_CLASS': 'api.paginators.StandardResultsSetPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    #     'rest_framework_social_oauth2.authentication.SocialAuthentication',
    # ),
}


# This setting is IMPORTANT: without it, rest_framework.reverse.reverse, which is
# also used in related fields, and which invokes request.build_absolute_uri, will
# never be able to set the correct protocol/scheme for the absolute URLs that it
# generates. If the django server receives requests via a load balancer, make sure
# the balancer forwards the protocol, e.g.
# proxy_set_header X-Forwarded-Proto $scheme;
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
