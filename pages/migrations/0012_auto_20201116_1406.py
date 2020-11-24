# Generated by Django 2.2 on 2020-11-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20201116_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='page',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='pageblock',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='review',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='slideritem',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='position',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Позиция'),
        ),
    ]
