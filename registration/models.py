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


class Name(models.Model):
    child_name = models.CharField(
        max_length=256,
        verbose_name="Çocuk Ad Soyad",
        help_text="Çocuk Ad Soyad\nChild's Name Surname\nИмя ребенка Фамилия",
    )
    child_age = models.PositiveSmallIntegerField(
        verbose_name="Yaş / Age / ВОЗРАСТ",
        help_text="Yaş / Age / ВОЗРАСТ",
    )
    permission_leave = models.BooleanField(
        default=False,
        verbose_name="Yalnız Gidebilir mi ?",
        help_text="Yalnız Gidebilir mi ?\nCan child leave the club alone ?\nМожет ли ребенок покинуть клуб один?"
    )
    diseases_allergy = models.CharField(
        max_length=256,
        default='YOK\nNone\nНету',
        verbose_name='Hastalık / Alerji\nDiseases/ Allergy\nЗаболевание / Аллергия',
        help_text='Hastalık / Alerji\nDiseases/ Allergy\nЗаболевание / Аллергия'
    )
    parents_name = models.CharField(
        max_length=512,
        verbose_name="Ebeveyn Ad Soyad\nParents' Name Surname\nИмя и фамилия родителей",
        help_text="Ebeveyn Ad Soyad\nParents' Name Surname\nИмя и фамилия родителей"
    )
    phone_number1 = models.CharField(
        max_length=25,
        verbose_name='Telefon   Numarası\nPhone Number\nTелефонный номер',
        help_text='Telefon   Numarası\nPhone Number\nTелефонный номер'
    )
    phone_number2 = models.CharField(
        max_length=25,
        verbose_name='Telefon   Numarası\nPhone Number\nTелефонный номер',
        help_text='Telefon   Numarası\nPhone Number\nTелефонный номер'
    )
    room_number = models.CharField(
        max_length=4,
        verbose_name='Oda No',
        help_text='Oda No\nRoom Number\nНомер комнаты'
    )
    check_out_date = models.DateField(
        verbose_name='Çıkış Tarihi/\nHotel Check-out Date /\nДата выезда из отеля',
        help_text='Çıkış Tarihi/\nHotel Check-out Date /\nДата выезда из отеля'
    )

    permission_foto = models.BooleanField(
        verbose_name='Foto izin\nРазрещение на фотографии',
        default=True
    )
    permission_activiti = models.BooleanField(
        verbose_name='Atöliyeye katılım izin\n Разщенение на мастер-класс',
        default=True
    )

    def __str__(self):
        if self.permission_leave:
            return f"Name :{self.child_name}\n Room number: {self.room_number}\n Permission : ÇIKABİLİR"
        return f"Name :{self.child_name}\n Room number: {self.room_number}\n Permission : ÇIKAMAZ "
