from django import forms
from django.contrib.auth import authenticate


class UserAuthForm(forms.Form):
    """Returns a token for authenticating requests of corresponding user instance.
    """
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)

    # def validate(self, data):
    #     email = data.get('email')
    #     password = data.get('password')

    #     if email and password:
    #         client = self.authenticate(email=email, password=password)

    #         if not client:
    #             msg = 'Unable to log in with provided credentials.'
    #             raise forms.ValidationError(msg)
    #     else:
    #         msg = 'Must include "email" and "password".'
    #         raise forms.ValidationError(msg)

    #     data['user'] = client
    #     return data

    # def authenticate(self, email, password):
    #     client = authenticate(username=email, password=password)
    #     return client
