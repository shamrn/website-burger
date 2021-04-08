from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy



class Profile(models.Model):
    email = models.EmailField(verbose_name='E-mail')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.IntegerField(verbose_name='Номер',null=True)
    bonuses = models.IntegerField(default=0,verbose_name='Баллы')
    name = models.CharField(null=True,max_length=50,verbose_name='ФИО')
    address = models.CharField(null=True,max_length=50,verbose_name='Адрес доставки')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.user.username


