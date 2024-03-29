# Generated by Django 3.1.7 on 2021-02-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymenu',
            options={'verbose_name': 'Категорию Меню', 'verbose_name_plural': 'Категорий Меню'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('category',), 'verbose_name': 'Меню', 'verbose_name_plural': 'Меню'},
        ),
        migrations.AddField(
            model_name='menu',
            name='show_ingridients',
            field=models.BooleanField(default=False, verbose_name='Добавить состав'),
        ),
    ]
