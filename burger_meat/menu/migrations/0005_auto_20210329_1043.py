# Generated by Django 3.1.7 on 2021-03-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20210316_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='ingredient',
            field=models.ManyToManyField(blank=True, to='menu.Ingridients', verbose_name='Ингредиент'),
        ),
    ]
