# Generated by Django 2.2 on 2020-11-18 00:43

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_navigationlinks_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationlinks',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=100, region=None, verbose_name='Телефон'),
        ),
    ]