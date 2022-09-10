from django.shortcuts import render
from django.views.generic import View
from registration.models import Name


class Home(View):
    def get(self, request):
        return render(request=request, template_name="registration/index.html")
