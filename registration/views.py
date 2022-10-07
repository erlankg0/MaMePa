from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from registration.forms import AddChildForm, PersonAdd
from django.core.mail import send_mail
from mamepa.settings import EMAIL_HOST_USER


# Main Page
class Home(View):
    def get(self, request):
        return render(request=request, template_name="registration/index.html")


class Admin(View):
    def get(self, request):
        return render(request, "admin_login.html")


class BabySitting(TemplateView):
    template_name = "registration/baby_sitting.html"


class PersonAdd(FormView):
    form_class = PersonAdd
    template_name = "registration/form_register.html"
    success_url = "add_child"

    def form_valid(self, form):
        form.save()
        return super(PersonAdd, self).form_valid(form)


class ChildAdd(FormView):
    form_class = AddChildForm  # Child Form
    template_name = "registration/form_register.html"  # HTML template
    success_url = "/"

    def form_valid(self, form):
        if int(self.request.POST.get("child_age")) <= 3:
            return redirect("baby_sitting")

        if self.request.POST.get("parents_email") != "example@exmaple.com":
            send_mail('Добро пожаловать в наш семейный клуб MaMepa!',
                      "Имя Фамилия ребёнка {0} {1} Isim Soyisim {0} {1} Name Surname {0} {1}".format(
                          self.request.POST.get('child_name'), self.request.POST.get('child_surname')),
                      EMAIL_HOST_USER,
                      [str(self.request.POST.get('parents_email'))],
                      False
                      # to email
                      )
            # send_mail("", "", "", [""], False)
            form.save()
        return super(ChildAdd, self).form_valid(form)


# data = {
# ...     'child_name' : 'Daniela',
# ...     'child_surname' : 'Abdraimoe',
# ...     'child_age' : 10,
# ...     'permission_foto': 'YES',
# ...     'permission_activiti': 'NO',
# ...     'permission_leave': 'NO',
# ...     'parents_name': 'Sakena',
# ...     'parents_surname': 'Abdykerimova',
# ...     'diseases_allergy' : 'YOK',
# ...     'phone1' : '_54t545',
# ...     'phone2' : '54565465656',
# ...     'check_out_date': '2023-01-01'
# ... }


def add_child(request):
    form = ChildAdd()
    if request.method == "POST":
        pass
    return render(request, "registration/form_register.html", {})
