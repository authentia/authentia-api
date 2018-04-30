from django.urls import path

from companies.views import validations
from users.views import verification

urlpatterns = [
    # path('authentication/', verification.UserLogin.as_view(), name='authentication'),
    # path('<token>/verification/', verification.UserVerificationView.as_view(), name='verification'),
]

