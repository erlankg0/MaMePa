from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import View, FormView
from registration.models import Registration
from registration.forms import RegistrationForm


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
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('/')
    context = {
        'forms': form
    }

    return render(request, 'registration/forms.html', context)