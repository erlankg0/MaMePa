from django.contrib import admin
from django.utils.safestring import mark_safe
from registration.models import Child, Person, FeedBack


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'age',
        'phone',
        'position',

    )
    list_display_links = (
        'name',
        'surname',
        'age',
        'phone',
        'position',
    )
    search_fields = (
        'name',
        'surname',
        'age',
        'phone',
        'position',
    )
    prepopulated_fields = {'slug': ('name', 'surname', 'age', 'position')}

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe('<img src="{0}" width="90">').format(obj.photo)
        else:
            return '-'


@admin.register(Child)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (

        'child_name',
        'child_age',
        "room_number",
        "permission_leave",
        'check_out_date',
        'phone1',
        'phone2',

    )
    list_filter = [
        "room_number",
        'check_out_date',
    ]
    search_fields = (
        "room_number",
        "permission_leave",
        'check_out_date',
        'child_name',
        'phone1',
        'phone2',
    )
    list_editable = (
        'permission_leave',
        'phone1',
        'phone2',
    )

    def get_photo(self, obj):
        if obj.child_photo:
            return mark_safe('<img src="{0}" width="90">').format(obj.child_photo)
        else:
            return '-'
