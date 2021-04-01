from django.db import models
from menu.models import Menu
from account.models import Profile


class Order(models.Model):

    STATUS_CHOICES = (
        ('1','Отменен'),
        ('2','Реализован'),
        ('3','В работе'),
    )

    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,verbose_name='Пользователь')
    name = models.CharField(max_length=55,verbose_name='ФИО')
    address = models.CharField(max_length=55,verbose_name='Адрес доставки')
    phone = models.IntegerField(verbose_name='Номер')
    created = models.DateTimeField(auto_now_add=True,null=True,verbose_name='Дата создания заказа')
    status_order = models.CharField(max_length=40,default='3',choices=STATUS_CHOICES,verbose_name='Статус заказа')


    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='Заказ')
    product = models.ForeignKey(Menu,on_delete=models.CASCADE,verbose_name='Товар')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1,verbose_name='Кол-во')

    class Meta:
        verbose_name = 'Товар'