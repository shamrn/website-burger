from django.db import models

class Shares(models.Model):
    STATUS_CHOICES = (
        ('draft','Черновик'),
        ('published','Опубликовано')
    )

    body = models.CharField(max_length=150,verbose_name='Описание акции')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

