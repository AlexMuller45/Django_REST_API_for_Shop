from django.contrib.auth.models import User

from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='ava/', blank=True, verbose_name='Аватарка')

    class Meta:
        verbose_name_plural = 'Профиль пользователя'
        verbose_name = 'Профили пользователей'

    def __str__(self):
        return self.user.username

    def full_name(self):
        return self.user.get_full_name()


class Address(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=CASCADE)
    city = models.ForeignKey(Cities, on_delete=PROTECT, verbose_name='Город')
    address = models.CharField(max_length=256, verbose_name='Адрес')

    def __str__(self):
        return '{}, {}'.format(self.city, self.address)


class Cities(models.Model):
    city = models.CharField(max_length=128, verbose_name='Город')

    def __str__(self):
        return self.city


class Payments(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название карты')
    number = models.CharField(max_length=19, verbose_name='Номер карты')
    name = models.CharField(max_length=128, blank=True, null=True, verbose_name='Имя владельца карты')
    month = models.IntegerField(max_length=2, verbose_name='Месяц окончания срока действия карты')
    year = models.IntegerField(max_length=2, verbose_name='Год окончания срока действия карты')
    code = models.IntegerField(max_length=3, verbose_name='Секретный код с обратной стороны карты')

    def __str__(self):
        return self.title

