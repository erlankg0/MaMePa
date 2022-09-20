from re import I
from django.shortcuts import render
from django.views.generic import View, FormView
from registration.models import Registration
from registration.forms import RegistrationForm


class Home(View):
    def get(self, request):
        return render(request=request, template_name="registration/index.html")


class RegisterPage(FormView):
    template_name = 'registration/form_register.html'
    form_class = RegistrationForm
    success_url = '/'


def registration_child(request):
    return render(request, 'registration/form_register.html')