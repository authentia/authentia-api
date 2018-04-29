from django import forms


class VerificationForm(forms.Form):
    file = forms.FileField()
