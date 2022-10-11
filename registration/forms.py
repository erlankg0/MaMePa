from django.forms import ModelForm, TextInput, Select, DateInput, FileInput, NumberInput, EmailInput, Textarea

from registration.models import Child, Person, FeedBack


# -------- Person form

class PersonAdd(ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'surname',
            'age',
            'position',
            'phone',
            'photo',
            'end_work',
        ]
        exclude = ['start_work']

        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                }
            ),
            'surname': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                }
            ),
            'age': NumberInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                }
            ),
            'position': Select(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                }
            ),
            'phone': TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                }
            ),
            'photo': FileInput(
                attrs={
                    'class': 'form-control',
                    'type': 'file',
                }
            ),
            'end_work': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }


# ------ Child form

class AddChildForm(ModelForm):
    required_attribute_css_class = 'col-sm-2 col-form-label'

    class Meta:
        model = Child
        fields = [
            'child_photo',
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
            'parents_email',
            'permission_activity',
            'permission_photo',
            'check_out_date',

        ]
        exclude = ['slug', ]

        widgets = {
            'child_photo': FileInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'type': 'file',
                }
            ),
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
            'parents_email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'Email Э-почта',
                    'value': 'example@exmaple.com',
                }
            ),
            "permission_photo": Select(
                attrs={
                    'id': 'selectPermissionFoto',
                    "class": "form-control",
                    "type": "text",
                    "title": "Разрешение на видеосъемку: Я разрешаю вам делать фотографии моего ребенка и использовать их в своих рекламных и материалах для печати или в Интернете.",
                }
            ),
            "permission_activity": Select(
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


# ----- FeedBack form

class AddFeedBack(ModelForm):
    class Meta:
        model = FeedBack
        fields = (
            'name',
            'phone',
            'email',
            'message',
        )

        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-input',
                    'id': "contact-name",
                    'type': "text",
                    'data-constraints': "@Required",
                }
            ),
            'phone': TextInput(
                attrs={
                    'class': "form-input",
                    'id': "contact-phone",
                    'typy': "text",
                    'name': "phone",
                    'data-constraints': "@Numeric",

                }
            ),
            'email': EmailInput(
                attrs={
                    'class': "form-input",
                    'id': "contact-email",
                    'type': "email",
                    'data-constraints': "@Email @Required",
                }
            ),
            'message': Textarea(
                attrs={
                    'class': "form-input",
                    'id': "contact-message",
                    'data-constraints': "@Required",
                }
            )
        }
