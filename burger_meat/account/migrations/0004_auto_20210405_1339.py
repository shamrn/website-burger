# Generated by Django 3.1.7 on 2021-04-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210405_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=50, null=True, verbose_name='Адрес доставки'),
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='ФИО'),
        ),
    ]
