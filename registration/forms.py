from dataclasses import fields
from pyexpat import model
from django import forms
from registration.models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = (
            'child',
            'parents',
            'permission_leave',
            'phone1',
            'phone2',
            'room_number',
            'check_out_date',
            'permission_foto',
            'permission_activiti',
        )

        widgets = {
            'child': forms.TextInput(
                attrs={"class": 'form-control'}
                ),
            'parents': forms.TextInput(
                attrs={"class": 'form-control'}
            ),
            
        }