# Generated by Django 2.2 on 2020-11-25 17:24

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20201121_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='preloader',
            field=models.ImageField(blank=True, null=True, upload_to=core.utils.image_path, verbose_name='Прелоадер сайта'),
        ),
    ]
