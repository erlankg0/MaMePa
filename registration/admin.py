from django.contrib import admin
from registration.models import Person, Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "room_number",
        "permission_leave",
    )
    list_filter = [
        "room_number",
    ]
    search_fields = (
        "room_number",
        "permission_leave",
    )
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


