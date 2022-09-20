from django.urls import path

from registration.views import Home, registration_child

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('registration/', registration_child, name='registration'),
]
