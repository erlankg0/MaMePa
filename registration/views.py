from django.shortcuts import render
from django.http import HttpResponse
import datetime
from registration.models import Name


def index(request):
    names = Name.objects.all()
    context = {
        "names": names
    }
    return render(request, "registration/index.html", context=context)
