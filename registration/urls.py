from django.urls import path
from registration.views import index

urlpatterns = [
    path('', index, name='home'),
]
