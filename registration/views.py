from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView

from registration.forms import AddChildForm, PersonForm


class Home(View):
    def get(self, request):
        return render(request=request, template_name="registration/index.html")


def add_person(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("child/add/1/")
    else:
        form = PersonForm()
        return render(request, 'registration/form_register.html', {'form': form})


class ChildDeatil(View):
    def get(self, request, child_id):
        return HttpResponse("Child_id {0}".format(child_id))


class AddPerson(TemplateView):
    template_name = 'registration/form_register.html'

    def get_context_data(self, *args, **kwargs):
        context['forms'] = PersonForm()
        return super().get_context_data()

    def post(self):
        form = PersonForm()
        if self.request.method == 'POST':
            form = PersonForm(self.request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = PersonForm()
            return render(self.request, template_name=self.template_name, context={'forms': form})


class ChildAdd(TemplateView):
    template_name = 'registration/form_register.html'

    def post(self, request):
        form = AddChildForm()
        if self.request.method == 'POST':
            form = AddChildForm(self.request.FILES)
