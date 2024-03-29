# Generated by Django 3.1.7 on 2021-02-24 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(db_index=True, max_length=50, verbose_name='Категория меню')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название продукта')),
                ('volume', models.CharField(blank=True, max_length=50, verbose_name='Объём продукта')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('photo', models.ImageField(upload_to='photos/<django.db.models.fields.related.ForeignKey>/', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.categorymenu', verbose_name='Категория меню')),
            ],
        ),
    ]
