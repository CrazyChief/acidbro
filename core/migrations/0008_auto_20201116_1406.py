# Generated by Django 2.2 on 2020-11-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201116_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationlinks',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
    ]
