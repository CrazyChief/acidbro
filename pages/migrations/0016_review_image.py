# Generated by Django 2.2 on 2020-11-21 18:42

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20201121_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.image_path, verbose_name='Изображение'),
        ),
    ]
