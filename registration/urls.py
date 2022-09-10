from django.urls import path
from registration.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
]
