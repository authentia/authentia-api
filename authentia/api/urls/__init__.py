from django.urls import path, include


urlpatterns = [
    path('users/', include('api.urls.authentia_users')),
    path('company-users/', include('api.urls.company_users')),
    path('document-types/', include('api.urls.document_types')),
    path('leads/', include('api.urls.leads')),
    path('companies/', include('api.urls.companies')),
]
