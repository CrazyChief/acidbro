from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

from .utils import image_path


class SiteSettings(models.Model):
    favicon = models.ImageField(
        _(u'Favicon (отображается во вкладке сайта)'),
        upload_to=image_path,
        null=True,
        blank=True
    )
    logo = models.ImageField(
        _(u'Логотип сайта'),
        upload_to=image_path,
    )
    preloader = models.ImageField(
        _(u'Прелоадер сайта'),
        upload_to=image_path,
        null=True,
        blank=True
    )
    first_background_color = ColorField(
        _(u'Первый цвет фона'),
        default='#FFFFFF'
    )
    second_background_color = ColorField(
        _(u'Второй цвет фона'),
        default='#FFFFFF'
    )

    class Meta:
        verbose_name = _(u'Настройка сайта')
        verbose_name_plural = _(u'Настройки сайта')


class HeaderSettings(models.Model):
    left_side_title = models.CharField(
        _(u'Заголовок страницы (левая сторона)'),
        max_length=50,
    )
    left_side_title_color = ColorField(
        _(u'Цвет заголовка страницы (левая сторона)'),
        default='#07187b'
    )
    right_side_title = models.CharField(
        _(u'Заголовок (правая сторона)'),
        max_length=100,
        blank=True
    )
    right_side_description = RichTextField(
        _(u'Описаниие'),
        blank=True
    )
    right_side_background_image = models.ImageField(
        _(u'Фоновое изображение (правая сторона)'),
        upload_to=image_path,
        null=True,
        blank=True
    )
    use_button = models.BooleanField(
        _(u'Отображать кнопку/ccылку? (правая часть)'),
        default=False
    )
    button_text = models.CharField(
        _(u'Текст кнопки'),
        max_length=50,
        null=True,
        blank=True
    )
    button_link = models.URLField(
        _(u'Ссылка кнопки'),
        null=True,
        blank=True
    )

    class Meta:
        abstract = True
        verbose_name = _(u'Настройка шапки сайта')
        verbose_name_plural = _(u'Настройки шапки сайта')


class FooterSettings(models.Model):
    country = models.CharField(
        _(u'Страна'),
        max_length=50,
        blank=True,
        null=True
    )
    state = models.CharField(
        _(u'Область'),
        max_length=50,
        blank=True,
        null=True
    )
    city = models.CharField(
        _(u'Город'),
        max_length=50,
        blank=True,
        null=True
    )
    address_1 = models.CharField(
        _(u'Адрес 1'),
        max_length=150,
        blank=True,
        null=True
    )
    address_2 = models.CharField(
        _(u'Адрес 2'),
        max_length=50,
        blank=True,
        null=True
    )
    zip_code = models.CharField(
        _(u'Почтовый индекс'),
        max_length=50,
        blank=True,
        null=True
    )

    text = RichTextField(_(u'Текст подвала'), blank=True, null=True)
    copyright_text = models.CharField(
        _(u'Текст копирайта'),
        max_length=50,
        default='Copyright'
    )
    background_color = ColorField(
        _(u'Фоновый цвет футера'),
        default='#021d6e'
    )
    footer_logo = models.ImageField(
        _(u'Логотип (подвал сайта)'),
        upload_to=image_path,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _(u'Подвал сайта')
        verbose_name_plural = _(u'Подвалы сайта')


class NavigationLinks(models.Model):
    LINK_TYPES = (
        (0, _(u'Произвольная')),
        (1, _(u'По ключу')),
        (2, _(u'Телефон')),
        (3, _(u'Емейл')),
    )
    navigation = models.ForeignKey(
        to='core.NavigationMenu',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    link_to = models.IntegerField(
        _(u'Тип ссылки'),
        default=1,
        choices=LINK_TYPES
    )
    link = models.URLField(
        _(u'Ссылка'),
        blank=True,
        null=True
    )
    page = models.ForeignKey(
        'pages.Page',
        on_delete=models.SET_NULL,
        verbose_name=_(u'Страница'),
        blank=True,
        null=True
    )
    name = models.CharField(
        _(u'Название'),
        max_length=100,
        blank=True,
        null=True
    )
    icon = models.ImageField(
        _(u'Иконка'),
        upload_to=image_path,
        blank=True,
        null=True
    )
    phone = PhoneNumberField(_(u'Телефон'), max_length=100, blank=True)
    use_in_slider = models.BooleanField(
        _(u'Использоватьт в слайдере'),
        default=False
    )
    slider_item = models.ForeignKey(
        to='pages.SliderItem',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    use_in_page_block = models.BooleanField(
        _(u' Использовать в блоке страницы'),
        default=False
    )
    page_block = models.ForeignKey(
        to='pages.PageBlock',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    publish = models.BooleanField(_(u'Публиковать'), default=False)
    position = models.PositiveIntegerField(
        _(u'Позиция'),
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['position']
        verbose_name = _(u'Навигационная ссылка')
        verbose_name_plural = _(u'Навигационные ссылки')

    def __str__(self):
        return f'NavigationLink {self.name}'

    def is_published(self):
        return self.publish

    is_published.admin_order_field = 'publish'
    is_published.boolean = True
    is_published.short_description = _(u'Опубликовано?')

    @property
    def get_link(self):
        if self.link_to == 0:
            return self.link
        elif self.link_to == 1:
            return reverse('page_detail', args=[self.page.slug])


class NavigationMenu(models.Model):
    MENU_TYPE_CHOICES = (
        (0, _(u'Основное меню')),
        (1, _(u'Подвал сайта')),
        (2, _(u'Подвал сайта (социальное меню)')),
        (3, _(u'Подвал сайта (номера телефонов/контакты)'))
    )

    name = models.CharField(
        _(u'Название'),
        max_length=100,
        blank=True,
        null=True
    )
    menu_type = models.IntegerField(
        _(u'Тип меню'),
        choices=MENU_TYPE_CHOICES,
        blank=True,
        null=True
    )
    text_color = ColorField(
        _(u'Цвет текста меню'),
        default='#090d5e',
    )
    footer = models.ForeignKey(
        to='core.FooterSettings',
        on_delete=models.SET_NULL,
        related_name='footer_menus',
        verbose_name=_(u'Меню подвала сайта'),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _(u'Навигационное меню')
        verbose_name_plural = _(u'Навигационные меню')

    def __str__(self):
        return f'{self.name}'
