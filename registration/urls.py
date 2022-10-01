from django.urls import path

from registration.views import Home, ChildDeatil, ChildAdd, AddPerson, add_person

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('child/<int:child_id>/', ChildDeatil.as_view(), name='child_id'),
    path('child/add', ChildAdd.as_view(), name='add_child'),
    path('person/add', add_person, name='add_person'),
]
