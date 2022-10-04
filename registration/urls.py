from django.urls import path

from registration.views import Home, ChildAdd

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('child/add', ChildAdd.as_view(), name='add_child'),
]
