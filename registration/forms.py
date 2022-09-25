from cProfile import label
from logging import PlaceHolder
from tkinter import Widget
from django import forms
from django.forms import TextInput

from registration.models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        # fields = (
        #     'child.name',
        #     'child.surname',
        #     'child.age',
        #     'parents',
        #     'permission_leave',
        #     'phone1',
        #     'phone2',
        #     'room_number',
        #     'check_out_date',
        #     'permission_foto',
        #     'permission_activiti',
        # )
        fields = "__all__"
        labels = {
            "child_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "inputChildName",
                }
            )
        }
        widgets = {
            "child_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Çocuk İsim. Child Name. Имя ребёнка",
                    "id": "inputChildName",
                    "type": "text",
                }
            ),
            "child_surname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Çocuk Soyisim. Child Surname. Фамилия ребёнка",
                    "id": "inputChildSurname",
                    "type": "text",
                }
            ),
            "child_age": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Çocuk Yaş. Child Age. Возраст ребёнка",
                    "id": "inputChildAge",
                    "type": "number",
                    "maxlength": "2",
                }
            ),
            "parents_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ebebeyin İsim. Parent's Name. Имя родителя",
                    "id": "inputParentsName",
                    "type": "text",
                }
            ),
            "parents_surname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ebebeyin Soyisim. Parent's Surname. Фамилия родителя",
                    "id": "inputParentsName",
                    "type": "text",
                }
            ),
            "diseases_allergy": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Hastalık ( Alergi ). Allergy ( Child ). Заболевния ( Аллергия ).",
                    "id": "inputAllergy",
                    "type": "text",
                }
            ),
            "permission_leave": forms.TextInput(
                attrs={
                    "class": "form-check-input",
                    "type": "radio",
                    "name": "leave-alone",
                    "id": "radio-leave-alone1",
                    "value": "True",
                }
            ),
            'room_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                    'name': 'inputRoomNumber',
                    'min' : 1000,
                    'max': 9999,
                    'placeholder': 'Oda no. Room Number. Номер комнаты',
                }
            ),
            'phone1': forms.TextInput(
                attrs={
                    "class": 'form-control',
                    'type': 'tel',
                    'name': 'inputPhoneNumber1',
                    'placeholder': 'Tel No. Phone Number. Номер телефона',

                }
            ),
            'phone2': forms.TextInput(
                attrs={
                    "class": 'form-control',
                    'type': 'tel',
                    'name': 'inputPhoneNumber1',
                    'placeholder': 'Tel No. Phone Number. Номер телефона',
                    
                }
            ),
            "permission_foto": forms.TextInput(
                attrs={
                    "class": "form-check-input",
                    "type": "radio",
                    "value": "True",
                }
            ),
            "permission_activiti": forms.TextInput(
                attrs={
                    "class": "form-check-input",
                    "type": "radio",
                    "value": "True",
                }
            ),
        }
