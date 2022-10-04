from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import FormView

from registration.forms import AddChildForm


# Main Page
class Home(View):
    def get(self, request):
        return render(request=request, template_name="registration/index.html")


class PersonAdd(FormView):


    pass


class ChildAdd(FormView):
    form_class = AddChildForm  # Child Form
    template_name = 'registration/form_register.html'  # HTML template
    success_url = '/'

    def form_valid(self, form):
        form.child_name = self.request.POST.get('child_name')
        form.child_surname = self.request.POST.get('child_surname')
        form.child_age = self.request.POST.get('child_age')
        form.permission_leave = self.request.POST.get('permission_leave')
        form.diseases_allergy = self.request.POST.get('diseases_allergy')
        form.parents_name = self.request.POST.get('parents_name')
        form.parents_surname = self.request.POST.get('parents_surname')
        form.phone1 = self.request.POST.get('phone1')
        form.phone2 = self.request.POST.get('phone2')
        form.permission_foto = self.request.POST.get('permission_foto')
        form.permission_activiti = self.request.POST.get('permission_activiti')
        form.check_out_date = self.request.POST.get('check_out_date')
        if form.child_age <= 3:
            return redirect('/')
        else:
            form.save()
        return super().form_valid(form)

#
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
