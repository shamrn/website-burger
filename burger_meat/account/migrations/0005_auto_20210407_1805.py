# Generated by Django 3.1.7 on 2021-04-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210405_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(null=True, verbose_name='Номер'),
        ),
    ]
