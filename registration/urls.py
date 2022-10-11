from django.urls import path

from registration.views import Home, ChildAdd, Admin, PersonAdd, BabySitting, Contacts

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('child/add', ChildAdd.as_view(), name='add_child'),
    path('extra/baby-sitting', BabySitting.as_view(), name='baby_sitting'),
    path('contacts', Contacts.as_view(), name='contacts'),
    path('newadmin', Admin.as_view()),
    path('person/add', PersonAdd.as_view(), name='persons'),
]
