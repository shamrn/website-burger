# Generated by Django 3.1.7 on 2021-03-13 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210226_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingridients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingridient', models.CharField(max_length=50, verbose_name='Ингредиент')),
            ],
        ),
        migrations.AlterModelOptions(
            name='categorymenu',
            options={'verbose_name': 'Категория меню', 'verbose_name_plural': 'Категории меню'},
        ),
        migrations.AlterField(
            model_name='categorymenu',
            name='category',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Категории меню'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menu.categorymenu', verbose_name='Категории меню'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='photo',
            field=models.ImageField(upload_to='photos/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='menu',
            name='ingridient',
            field=models.ManyToManyField(to='menu.Ingridients', verbose_name='Ингредиент'),
        ),
    ]