from django.contrib import admin
from registration.models import Registration


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


