from django import forms

from registration.models import Registration


class RegistraionFormV1(forms.Form):
    child_name = forms.CharField(
        max_length=256,
        min_length=4,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Çocuk İsim. Child Name. Имя ребёнка",
                "id": "inputChildName",
                "type": "text",
            }
        ),
    )
    child_surname = forms.CharField(max_length=256, min_length=4)
    child_age = forms.IntegerField(max_value=16, min_value=0)
    permission_leave = forms.BooleanField()
    diseases_allergy = forms.CharField(max_length=256, min_length=4)

    room_number = forms.IntegerField(min_value=1000, max_value=9999)

    parents_name = forms.CharField(max_length=256, min_length=4)
    parents_surname = forms.CharField(max_length=256, min_length=4)

    phone1 = forms.CharField(min_length=6, max_length=20)
    phone2 = forms.CharField(min_length=6, max_length=20)

    check_outdate = forms.DateField(required=True)

    widgets = {
       
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
                "type": "checkbox",
                "value": "True",
            }
        ),
        "room_number": forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "number",
                "name": "inputRoomNumber",
                "min": 1000,
                "max": 9999,
                "placeholder": "Oda no. Room Number. Номер комнаты",
            }
        ),
        "phone1": forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "tel",
                "name": "inputPhoneNumber1",
                "placeholder": "Tel No. Phone Number. Номер телефона",
            }
        ),
        "phone2": forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "tel",
                "name": "inputPhoneNumber1",
                "placeholder": "Tel No. Phone Number. Номер телефона",
            }
        ),
        "permission_foto": forms.TextInput(
            attrs={
                "class": "form-check-input",
                "type": "checkbox",
                "value": "True",
                "title": "Разрешение на видеосъемку: Я разрешаю вам делать фотографии моего ребенка и использовать их в своих рекламных и материалах для печати или в Интернете.",
            }
        ),
        "permission_activiti": forms.TextInput(
            attrs={
                "title": "Я разрешаю своему ребенку самому посещать семинары в семейном клубе Ma&Me&Pa, использовать соответствующие  материалы / инструменты и проводить свободное время на игровой площадке. ВСЯ ОТВЕТСТВЕННОСТЬ ЛЕЖИТ НА МНЕ.",
                "class": "form-check-input",
                "type": "checkbox",
                "value": "True",
            }
        ),
    }


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
            # "permission_leave": forms.TextInput(
            #     attrs={
            #         "class": "form-check-input",
            #         "type": "radio",
            #         "name": "leave-alone",
            #         "id": "radio-leave-alone1",
            #         "value": "True",
            #     }
            # ),
            "room_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "number",
                    "name": "inputRoomNumber",
                    "min": 1000,
                    "max": 9999,
                    "placeholder": "Oda no. Room Number. Номер комнаты",
                }
            ),
            "phone1": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                    "name": "inputPhoneNumber1",
                    "placeholder": "Tel No. Phone Number. Номер телефона",
                }
            ),
            "phone2": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                    "name": "inputPhoneNumber1",
                    "placeholder": "Tel No. Phone Number. Номер телефона",
                }
            ),
            # "permission_foto": forms.TextInput(
            #     attrs={
            #         "class": "form-check-input",
            #         "type": "radio",
            #         "value": "True",
            #         "title": "Разрешение на видеосъемку: Я разрешаю вам делать фотографии моего ребенка и использовать их в своих рекламных и материалах для печати или в Интернете.",
            #     }
            # ),
            # "permission_activiti": forms.TextInput(
            #     attrs={
            #         "title": "Я разрешаю своему ребенку самому посещать семинары в семейном клубе Ma&Me&Pa, использовать соответствующие  материалы / инструменты и проводить свободное время на игровой площадке. ВСЯ ОТВЕТСТВЕННОСТЬ ЛЕЖИТ НА МНЕ.",
            #         "class": "form-check-input",
            #         "type": "radio",
            #         "value": "True",
            #     }
            # ),
        }
