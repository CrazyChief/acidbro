# Generated by Django 2.2 on 2020-11-13 05:02

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20201104_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageblock',
            name='publish',
            field=models.BooleanField(default=False, verbose_name='Публиковать'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.image_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='page',
            name='right_side_background_image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.image_path, verbose_name='Фоновое изображение (правая сторона)'),
        ),
        migrations.AlterField(
            model_name='pageblock',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.image_path, verbose_name='Фоновое изображение'),
        ),
    ]
