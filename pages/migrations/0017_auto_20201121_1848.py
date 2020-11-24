# Generated by Django 2.2 on 2020-11-21 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.AlterField(
            model_name='review',
            name='company',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Компания, или должность (краткое описание)'),
        ),
        migrations.AlterField(
            model_name='review',
            name='company_en',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Компания, или должность (краткое описание)'),
        ),
        migrations.AlterField(
            model_name='review',
            name='company_ru',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Компания, или должность (краткое описание)'),
        ),
    ]
