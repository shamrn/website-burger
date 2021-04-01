from django.db import models

class CategoryMenu(models.Model):
    category = models.CharField(max_length=50,db_index=True,verbose_name='Категории меню')

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'

class Menu(models.Model):
    category = models.ForeignKey(CategoryMenu,on_delete=models.PROTECT,verbose_name='Категории меню')
    name = models.CharField(max_length=50,verbose_name='Название продукта')
    volume = models.CharField(max_length=50,blank=True,verbose_name='Объём продукта')
    price = models.IntegerField(blank=True,verbose_name='Цена')
    show_ingridients = models.BooleanField(default=False,verbose_name='Добавить состав')
    ingredient = models.ManyToManyField('Ingridients',blank=True,verbose_name='Ингредиент')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to=f'photos/',verbose_name='Изображение')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ('category',)

    def __str__(self):
        return self.name


class Ingridients(models.Model):
    ingredient = models.CharField(max_length=50,verbose_name='Ингредиент')

    def __str__(self):
        return self.ingredient

    class Meta:
        verbose_name = "Состав"
        verbose_name_plural = 'Ингредиенты'

