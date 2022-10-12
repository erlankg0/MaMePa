from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView

from mamepa.settings import EMAIL_HOST_USER
from registration.forms import AddChildForm, PersonAdd, AddFeedBack
from registration.models import Person


# Admin custom page
class Admin(View):
    def get(self, request):
        return render(request, "admin_login.html")


# Main Page
class Home(View):
    def get(self, request):
        return render(request=request, template_name="registration/index.html")


# Child add Page
class ChildAdd(FormView):
    form_class = AddChildForm  # Child Form
    template_name = "registration/form_register.html"  # HTML template
    success_url = "/"

    def form_valid(self, form):
        if int(self.request.POST.get("child_age")) <= 3:
            return redirect("baby_sitting")
        try:
            if self.request.POST.get("parents_email") != "example@exmaple.com":
                send_mail('Добро пожаловать в наш семейный клуб MaMepa!',
                          "Имя Фамилия ребёнка {0} {1} Isim Soyisim {0} {1} Name Surname {0} {1}\n Если ребёнок не может самостоятельно покинуть клуб. Про контролируйте что у него есть браслет!!!".format(
                              self.request.POST.get('child_name'), self.request.POST.get('child_surname')),
                          EMAIL_HOST_USER,
                          [str(self.request.POST.get('parents_email'))],
                          False
                          # to email
                          )
                form.save()
        except ValueError('Ошибка регистрации'):
            form.save()
        return super(ChildAdd, self).form_valid(form)


# Contacts Page
class Contacts(FormView):
    template_name = 'registration/contacts.html'
    form_class = AddFeedBack
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(Contacts, self).form_valid(form)


# Team Page
class Team(View):
    def get(self, request):
        personals = Person.objects.all()
        context = {'personals': personals}
        return render(request, 'registration/team.html', context)


# Baby Page
class BabySitting(FormView):
    template_name = "registration/baby_sitting.html"


# Person add Page(person/add)
class PersonAdd(FormView):
    form_class = PersonAdd
    template_name = "registration/form_register.html"
    success_url = "add_child"

    def form_valid(self, form):
        form.save()
        return super(PersonAdd, self).form_valid(form)
