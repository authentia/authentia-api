from django.urls import path

from companies.views import companies as views

urlpatterns = [
    path('', views.CompanyListCreateView.as_view()),
    path('<int:pk>/', views.CompanyRetrieveUpdateDestroyView.as_view()),
    path('<token>/verification/', views.UserVerificationView.as_view(), name='verification'),

]
