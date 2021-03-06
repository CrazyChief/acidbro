# Generated by Django 2.2 on 2020-11-21 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_review_publish'),
        ('core', '0013_auto_20201118_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationlinks',
            name='page_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.PageBlock'),
        ),
        migrations.AddField(
            model_name='navigationlinks',
            name='slider_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pages.SliderItem'),
        ),
        migrations.AddField(
            model_name='navigationlinks',
            name='use_in_page_block',
            field=models.BooleanField(default=False, verbose_name=' Использовать в блоке страницы'),
        ),
        migrations.AddField(
            model_name='navigationlinks',
            name='use_in_slider',
            field=models.BooleanField(default=False, verbose_name='Использоватьт в слайдере'),
        ),
    ]
