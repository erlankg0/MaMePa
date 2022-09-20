from django.contrib import admin
from registration.models import Registration, Child, Parents


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


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'age',
    )
    list_filter = (
        'age',
    )
    search_fields = (
        'name',
        'surname',
    )


# admin.site.register(Registration, RegistrationAdmin)
# Register your models here.
# admin.site.register(Child)
admin.site.register(Parents)
# admin.site.register(Registration)
