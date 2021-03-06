from django.urls import path

from users.views import company_users as views
from companies.views import companies as c_views
from companies.views import company_documents as d_views

urlpatterns = [
    path('', views.CompanyUserListCreateView.as_view()),
    path('<int:pk>/', views.CompanyUserRetrieveUpdateDestroyView.as_view()),
    path('auth/', views.CompanyUserAuthView.as_view()),
    path('companies/', c_views.CompanyListCreateView.as_view()),
    path('documents/', d_views.CompanyDocumentListCreateView.as_view()),
]
