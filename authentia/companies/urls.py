from django.urls import path

from companies.views import validations

urlpatterns = [
    path('authentication/', validations.UserLogin.as_view(), name='authentication'),
    path('<token>/verification/', validations.UserVerification.as_view(), name='verification'),
]

