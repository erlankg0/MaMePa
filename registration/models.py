from django.db import models

"""
Child Name char(256)
Child age SmallInt
Permission (Can child leave the club alone ?) Bool default False
Diseases/ Allergy Char
Parents name`s CharField
Check-out-date from hotel date
Room number

Permission_foto
Permission_activiti 

Signature


"""


class Person(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Ad\nName\nИмя",
        help_text="Ad\nName\nребёнка",
    )
    surname = models.CharField(
        max_length=256,
        verbose_name="Soyad\nSurname\nФамилия",
    )


# Registration MaMePa Guests

class Child(Person):
    age = models.PositiveSmallIntegerField(
        verbose_name="Yaş / Age / ВОЗРАСТ",
        help_text="Yaş / Age / ВОЗРАСТ",
    )
    diseases_allergy = models.CharField(
        max_length=256,
        default='YOK\nNone\nНету',
        verbose_name='Hastalık / Alerji\nDiseases/ Allergy\nЗаболевание / Аллергия',
        help_text='Hastalık / Alerji\nDiseases/ Allergy\nЗаболевание / Аллергия'
    )

    def __str__(self):
        return f'Name {self.name} {self.surname} age {self.age} allergy {self.diseases_allergy}'


class Parents(Person):

    def __str__(self):
        return f'{self.name} {self.surname}'


class Registration(models.Model):
    child = models.ForeignKey(
        Child,
        on_delete=models.CASCADE
    )
    parents = models.ForeignKey(
        Parents,
        on_delete=models.CASCADE
    )
    phone1 = models.CharField(
        max_length=20,
        verbose_name="Tel No\n Phone number\n Тел. номер",
        help_text="+X(XXX)XXX-XXX-XXX",
        unique=True
    )
    phone2 = models.CharField(
        max_length=20,
        verbose_name="Tel No\n Phone number\n Тел. номер",
        help_text="+X(XXX)XXX-XXX-XXX",
        unique=True
    )
    room_number = models.CharField(
        max_length=5,
        verbose_name='Oda no\n Room number\n Номер комнаты',
        help_text='Oda no\n Room number\n Номер комнаты'
    )
    permission_leave = models.BooleanField(
        default=False,
        verbose_name="Yalnız Gidebilir mi ?",
        help_text="Yalnız Gidebilir mi ?\nCan child leave the club alone ?\nМожет ли ребенок покинуть клуб один?"
    )
    permission_foto = models.BooleanField(
        verbose_name='Foto izin\nРазрещение на фотографии',
        default=True
    )
    permission_activiti = models.BooleanField(
        verbose_name='Atöliyeye katılım izin\n Разщенение на мастер-класс',
        default=True
    )
    check_out_date = models.DateField(
        verbose_name='Çıkış Tarihi/\nHotel Check-out Date /\nДата выезда из отеля',
        help_text='Çıkış Tarihi/\nHotel Check-out Date /\nДата выезда из отеля'
    )

    def __str__(self):
        if self.permission_leave:
            return f"Name :{self.child.name}\n Room number: {self.room_number}\n Permission : ÇIKABİLİR"
        return f"Name :{self.child.name}\n Room number: {self.room_number}\n Permission : ÇIKAMAZ "


