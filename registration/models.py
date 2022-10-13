from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


# ---------- PERSON

# ID - INT
# name - Varchar
# surname - Varchar
# age - Int
# photo - Img(Varchar)
# position - Varchar (choice)
# phone - Varchar


class Person(models.Model):
    POSITION = (
        ('Departman Animasiyon Müdürü', 'DIR'),
        ('Animasiyon Şef', 'SEF'),
        ('Animasiyon Şef Asistan', 'ASEF'),
        ('Animatör', 'ANI'),
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Isim\n Имя\n Name'
    )
    surname = models.CharField(
        max_length=30,
        verbose_name='Soyisim\n Фамилия\n Surname'
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Yaş\n Age\n Возвраст'
    )
    photo = models.ImageField(
        verbose_name='Photo\nResimi\nФотография',
        upload_to='%Y/%m/%d',
        blank=True,
        null=True,
    )
    position = models.CharField(
        max_length=100,
        choices=POSITION,
        verbose_name='Position\n Должность'
    )
    phone = models.CharField(
        max_length=256,
        verbose_name='Tel No:\n Номер телефона'
    )
    facebook = models.CharField(
        max_length=256,
        verbose_name='Facebook(URL)',
        blank=True,
        null=True,
    )
    instagram = models.CharField(
        max_length=256,
        verbose_name='Instargram',
        blank=True,
        null=True,
    )
    start_work = models.DateField(
        auto_now_add=True
    )
    end_work = models.DateField(
        blank=True, null=True
    )
    slug = models.SlugField(
        verbose_name='URL',
        unique=True
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify((self.name, self.surname, self.age, self.position))
        super(Person, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return '{0} {1} Tel No| {2}'.format(self.name, self.surname, self.phone)

    def get_absolute_url(self):
        return reverse('persons', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Personal Kayıt.\nPersonal Registration\nРегистрация персонала'
        verbose_name_plural = "Personal Kayıtlar.\nPersonal Registration's\nРегистрации персонала"


# ----------- Child`s


# child_photo Varchar
# child_name Varchar(256)
# child_surname Varchar(256)
# child_age Int
# diseases_allergy Varchar(256)
# permission_leave Boolean
# parents_name Varchar(256)
# parents_surname Varchar(256)
# parents_email Varchar(email)
# phone1 Varchar (256)
# phone2Varchar (256)
# permission_photo Boolean
# permission_activity Boolean


class Child(models.Model):
    # Choice
    YES_OR_NO = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )
    child_photo = models.ImageField(
        verbose_name='Photo\nResimi\nФотография',
        upload_to='%Y/%m/%d',
        blank=True,
        null=True,
    )
    child_name = models.CharField(
        max_length=256,
        verbose_name="Ad\nName\nИмя",
    )
    child_surname = models.CharField(
        max_length=256,
        verbose_name="Soyad\nSurname\nФамилия",
    )
    child_age = models.PositiveSmallIntegerField(
        verbose_name="Yaş / Age / ВОЗРАСТ",
    )
    diseases_allergy = models.CharField(
        max_length=256,
        default='YOK\nNone\nНету',
        verbose_name='Hastalık / Alerji\nDiseases/ Allergy\nЗаболевание / Аллергия',

    )
    parents_name = models.CharField(
        max_length=256,
        verbose_name="Ad\nName\nИмя",

    )
    parents_surname = models.CharField(
        max_length=256,
        verbose_name="Soyad\nSurname\nФамилия",
    )
    parents_email = models.EmailField(
        max_length=256,
        verbose_name='Email\n Э-почта',
        blank=True,
        null=True
    )
    phone1 = models.CharField(
        max_length=20,
        verbose_name="Tel No\n Phone number\n Тел. номер +X(XXX)XXX-XXX-XXX",
        unique=True
    )
    phone2 = models.CharField(
        max_length=20,
        verbose_name="Tel No\n Phone number\n Тел. номер +X(XXX)XXX-XXX-XXX",
        unique=True,
        blank=True,
        null=True,
    )
    room_number = models.CharField(
        max_length=5,
        verbose_name='Oda no\n Room number\n Номер комнаты',
    )
    permission_leave = models.CharField(
        max_length=3,
        choices=YES_OR_NO,
        verbose_name="Yalnız Gidebilir mi ?",
    )
    permission_photo = models.CharField(
        max_length=3,
        verbose_name='Foto izin\nРазрещение на фотографии',
        choices=YES_OR_NO

    )
    permission_activity = models.CharField(
        max_length=3,
        verbose_name='Atöliyeye katılım izin\n Разщенение на мастер-класс',
        choices=YES_OR_NO
    )
    check_out_date = models.DateField(
        verbose_name='Çıkış Tarihi/\nHotel Check-out Date /\nДата выезда из отеля',
    )
    slug = models.SlugField(verbose_name='URL', unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify((self.child_name, self.child_surname, self.room_number))
        super(Child, self).save(*args, **kwargs)

    def __str__(self):
        if self.permission_leave:
            return "Name :{0}\n Room number: {1}\n Permission : ÇIKABİLİR".format(self.child_name, self.room_number)
        return "Name :{0}\n Room number: {1}\n Permission : ÇIKAMAZ ".format(self.child_name, self.room_number)

    class Meta:
        ordering = ['check_out_date']
        verbose_name = 'Çocuk Kayıt.\nChild Registration\nРегистрация ребенка'
        verbose_name_plural = "Çocuk Kayıtlar.\nChild Registration's\nРегистрации детей"


#   ------- FeedBack
# Name Varchar(256)
# Email Varchar(256)
# phone Varchar(256)
# message Text

class FeedBack(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Name Surname İsim Soysism Имя Фамилия'
    )
    email = models.EmailField(
        max_length=256,
        verbose_name='E-mail'
    )
    phone = models.CharField(
        max_length=30,
        verbose_name='Phone Tel No Номер телефона'
    )
    message = models.TextField(
        max_length=5000,
        verbose_name="Message Сообщение"
    )
    date = models.DateField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Geri Dönüşüm'
        verbose_name_plural = "Geri Dönüşümler"
        ordering = ['-date']

    def __str__(self):
        return "{0} {1} Tarih {2}".format(self.name, self.email, self.date)
