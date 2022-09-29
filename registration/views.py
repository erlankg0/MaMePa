import re
from django.shortcuts import render, redirect
from django.views.generic import View, FormView

from registration.forms import RegistrationForm, RegistraionFormV1


class Home(View):
    def get(self, request):
        return render(request=request, template_name="registration/index.html")


class RegisterPage(FormView):
    # template_name = 'registration/form_register.html'
    template_name = 'registration/forms.html'
    form_class = RegistrationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')


def registration_child(request):
    if request.method == 'POST':
        form = RegistraionFormV1(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                return redirect('home')
            except Exception:
                form.add_error(None, 'Ошибка регистрации!')
    else:
        form = RegistraionFormV1()
    return render(request, 'registration/form_register.html', context={
        "forms": form
    })
