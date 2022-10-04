from dataclasses import fields
from django.forms import ModelForm, TextInput, Select, DateInput

from registration.models import Registration, Person


class PersonAdd(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class AddChildForm(ModelForm):
    class Meta:
        model = Registration
        fields = [
            'child_name',
            'child_surname',
            'child_age',
            'permission_leave',
            'diseases_allergy',
            'parents_name',
            'parents_surname',
            'room_number',
            'phone1',
            'phone2',
            'permission_activiti',
            'permission_foto',
            'check_out_date',

        ]
        exclude = ['slug', ]

        widgets = {
            "child_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Çocuk İsim. Child Name. Имя ребёнка",
                    "id": "inputChildName",
                    "type": "text",
                }
            ),
            "child_surname": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Çocuk Soyisim. Child Surname. Фамилия ребёнка",
                    "id": "inputChildSurname",
                    "type": "text",
                }
            ),
            "child_age": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Çocuk Yaş. Child Age. Возраст ребёнка",
                    "id": "inputChildAge",
                    "type": "number",
                    "maxlength": "2",
                }
            ),
            "parents_name": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ebebeyin İsim. Parent's Name. Имя родителя",
                    "id": "inputParentsName",
                    "type": "text",
                }
            ),
            "parents_surname": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ebebeyin Soyisim. Parent's Surname. Фамилия родителя",
                    "id": "inputParentsName",
                    "type": "text",
                }
            ),
            "diseases_allergy": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Hastalık ( Alergi ). Allergy ( Child ). Заболевния ( Аллергия ).",
                    "id": "inputAllergy",
                    "type": "text",
                }
            ),
            "permission_leave": Select(
                attrs={
                    "id": "selectLeaveAlone",
                    "class": "form-control",
                    "type": "text",
                }
            ),
            "room_number": TextInput(
                attrs={
                    "class": "form-control",
                    "type": "number",
                    "id": "inputRoomNumber",
                    "min": 1000,
                    "max": 9999,
                    "placeholder": "Oda no. Room Number. Номер комнаты",
                }
            ),
            "phone1": TextInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                    "id": "inputPhoneNumber1",
                    "placeholder": "Tel No. Phone Number. Номер телефона",
                }
            ),
            "phone2": TextInput(
                attrs={
                    "class": "form-control",
                    "type": "tel",
                    "id": "inputPhoneNumber1",
                    "placeholder": "Tel No. Phone Number. Номер телефона",
                }
            ),
            "permission_foto": Select(
                attrs={
                    'id': 'selectPermissionFoto',
                    "class": "form-control",
                    "type": "text",
                    "title": "Разрешение на видеосъемку: Я разрешаю вам делать фотографии моего ребенка и использовать их в своих рекламных и материалах для печати или в Интернете.",
                }
            ),
            "permission_activiti": Select(
                attrs={
                    'id': 'selectPermissionActivity',
                    "title": "Я разрешаю своему ребенку самому посещать семинары в семейном клубе Ma&Me&Pa, использовать соответствующие  материалы / инструменты и проводить свободное время на игровой площадке. ВСЯ ОТВЕТСТВЕННОСТЬ ЛЕЖИТ НА МНЕ.",
                    "class": "form-control",
                    "type": "text",
                }
            ),
            'check_out_date': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            )
        }
