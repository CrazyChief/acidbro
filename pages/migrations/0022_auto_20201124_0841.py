# Generated by Django 2.2 on 2020-11-24 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_auto_20201124_0435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='title',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='title_ru',
        ),
    ]
