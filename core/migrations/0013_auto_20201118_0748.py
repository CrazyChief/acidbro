# Generated by Django 2.2 on 2020-11-18 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_navigationlinks_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navigationlinks',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='navigationlinks',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='navigationlinks',
            name='slug_ru',
        ),
    ]
