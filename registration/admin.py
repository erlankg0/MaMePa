from django.contrib import admin
from registration.models import Name


class NameAdmin(admin.ModelAdmin):
    list_display = (
        "child_name",
        "parents_name",
        "room_number",
        "permission_leave",
    )
    list_filter = [
        "room_number",
    ]
    search_fields = (
        "child_name",
        "parents_name",
        "room_number",
        "permission_leave",
    )
admin.site.register(Name, NameAdmin)
# Register your models here.
