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


class Registration(models.Model):
    child_name = models.CharField(
        max_length=256,
        verbose_name="Ad\nName\nИмя",
        help_text="Ad\nName\nИмя",
    )
    child_surname = models.CharField(
        max_length=256,
        verbose_name="Soyad\nSurname\nФамилия",
    )
    child_age = models.PositiveSmallIntegerField(
        verbose_name="Yaş / Age / ВОЗРАСТ",
        help_text="Yaş / Age / ВОЗРАСТ",
    )
    diseases_allergy = models.CharField(
        max_length=256,
        default='YOK\nNone\nНету',
        verbose_name='Hastalık / Alerji\nDiseases/ Allergy\nЗаболевание / Аллергия',
        help_text='Hastalık / Alerji\nDiseases/ Allergy\nЗаболевание / Аллергия'
    )
    parents_name = models.CharField(
        max_length=256,
        verbose_name="Ad\nName\nИмя",
        help_text="Ad\nName\nФамилия",
    )
    parents_surname = models.CharField(
        max_length=256,
        verbose_name="Soyad\nSurname\nФамилия",
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
            return f"Name :{self.child_name}\n Room number: {self.room_number}\n Permission : ÇIKABİLİR"
        return f"Name :{self.child_name}\n Room number: {self.room_number}\n Permission : ÇIKAMAZ "

    class Meta:
        ordering = ['-room_number']
        verbose_name = 'Çocuk Kayıt.\nChild Registration\nРегистрация ребенка'
        verbose_name_plural = "Çocuk Kayıtlar.\nChild Registration's\nРегистрации детей"
