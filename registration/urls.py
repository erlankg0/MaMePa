from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from registration.views import Home, ChildAdd, Admin, PersonAdd, BabySitting, Contacts, Team

urlpatterns = [
                  path('', Home.as_view(), name='home'),
                  path('child/add', ChildAdd.as_view(), name='add_child'),
                  path('extra/baby_sitting', BabySitting.as_view(), name='baby_sitting'),
                  path('contacts', Contacts.as_view(), name='contacts'),
                  path('team', Team.as_view(), name='team'),
                  path('newadmin', Admin.as_view()),
                  path('person/add', PersonAdd.as_view(), name='persons'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
