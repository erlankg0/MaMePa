from django.urls import path

from registration.views import Home, ChildAdd, Admin, PersonAdd

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('child/add', ChildAdd.as_view(), name='add_child'),
    path('newadmin', Admin.as_view()),
    path('person/add', PersonAdd.as_view()),
]
