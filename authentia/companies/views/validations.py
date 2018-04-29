from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.views import LoginView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.core import signing

from companies.forms.authenticate import UserAuthForm
from companies.forms.verification import VerificationForm
from companies.models import Company, Transaction

class UserLogin(View):
    template_name = 'login.html'
    form_class = UserAuthForm

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        return render_to_response(self.get_context_data())

    def form_valid(self, form):
        print('valido')
        print (form.get_user())
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        print(form.errors)
        return render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('verification')


class UserVerification(FormView):
    """
    """
    template_name = 'verification.html'
    form_class = VerificationForm

    def get_success_url(self):
        return self.company.success_url

    def form_valid(self, form):
        file = form.cleaned_data.get('file')
        verify = self.request.user.verify_user(file)
        if verify.get('Errors'):
            context = {
                'message': verify.get('Errors').get('Message')
            }
            return self.render_to_response(context=context, form=form)
        elif 5 > verify.get('estimated') > 0:
            context['message'] = 'Not recognized'
            return self.render_to_response(context=context, form=form)
        Transaction.objects.create(user=self.request.user, company=self.company)
        return super().form_valid(form)


    def post(self, token, request, *args, **kwargs):
        print(request.user)
        self.request = request
        self.company = Company.objects.get(pk=signing.loads(token))
        return super().post(request, *args, **kwargs)

