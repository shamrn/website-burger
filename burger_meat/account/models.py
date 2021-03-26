from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.IntegerField(verbose_name='Номер')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
