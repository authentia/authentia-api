from django.urls import path, include


urlpatterns = [
    path('users/', include('api.urls.authentia_users')),
    path('document-types/', include('api.urls.document_types')),
]
