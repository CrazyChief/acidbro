from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField

from core.models import HeaderSettings
from core.utils import image_path
from seo.models import SeoMeta


class Page(SeoMeta, HeaderSettings):
    TEMPLATES = (
        (0, 'index.html'),
        (1, 'about.html'),
        (2, 'contact.html'),
        (3, 'news.html'),
        (4, 'portfolio.html'),
        (5, 'vacancies.html'),
        (6, '404.html'),
    )
    template = models.IntegerField(
        _(u'Шаблон страницы'),
        choices=TEMPLATES,
        blank=True,
        null=True
    )
    name = models.CharField(_(u'Название'), max_length=100)
    slug = models.SlugField(_(u'ЧПУ'), max_length=100, blank=True, null=True)
    publish = models.BooleanField(_(u'Публиковать'), default=False)
    position = models.PositiveIntegerField(
        _(u'Позиция'),
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['position']
        verbose_name = _(u'Страница')
        verbose_name_plural = _(u'Страницы')

    def __str__(self):
        return f'{self.name} page'

    def get_absolute_url(self):
        if not self.slug:
            return ''
        return reverse('page_detail', args=[self.slug])

    def is_published(self):
        return self.publish

    is_published.admin_order_field = 'publish'
    is_published.boolean = True
    is_published.short_description = _(u'Опубликовано?')


class PageBlockManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset()

    def published(self):
        return self.get_queryset().filter(publish=True)


class PageBlock(models.Model):
    PAGE_BLOCK_TYPE = (
        (0, 'careers_wrapper'),
        # (1, 'careers_item'),
        (1, 'news_wrapper'),
        (2, 'contact_wrapper'),  # No block, just display info in header right side
        (3, 'company_wrapper'),  # No block, just display info in header right side
        (4, 'second_wrapper'),   # use nested blocks
        (5, 'sector_wrapper'),  # use nested blocks
        (6, 'project_wrapper'),
        (7, 'cripto_wrapper'),
        (8, 'team_wrapper'),
        (9, 'benefit_wrapper'),
        # (11, 'benefit_item'),
        (10, 'investor_wrapper'),
        # (13, 'investor_item'),
        (11, 'nested_block'),   # use nested block and render like benefit/careers/investor/second/cripto item
    )
    block_type = models.IntegerField(
        _(u'Тип блока'),
        choices=PAGE_BLOCK_TYPE,
        blank=True,
        null=True
    )
    nested_block = models.ForeignKey(
        verbose_name=_(u'Вложенный блок'),
        to='self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    page_object = models.ForeignKey(
        verbose_name=_(u'Для страницы'),
        to=Page,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    title = models.CharField(
        _(u'Заголовок'),
        max_length=40
    )
    title_color = ColorField(
        _(u'Цвет заголовка'),
        default='#07187b'
    )
    subtitle = models.CharField(
        _(u'Подзаголовок'),
        max_length=100,
        blank=True,
        null=True
    )
    text = RichTextField(_(u'Текст'), blank=True, null=True)
    background_image = models.ImageField(
        _(u'Фоновое изображение'),
        upload_to=image_path,
        blank=True,
        null=True
    )
    use_slider = models.BooleanField(
        _(u'Использовать слайдер'),
        default=False
    )
    publish = models.BooleanField(_(u'Публиковать'), default=False)
    position = models.PositiveIntegerField(
        _(u'Позиция'),
        default=0,
        blank=True,
        null=True
    )

    objects = PageBlockManager()

    class Meta:
        ordering = ['position']
        verbose_name = _(u'Блок страницы')
        verbose_name_plural = _(u'Блоки страницы')

    def children(self):
        """
        Child pages.
        Ex. blog pages on blog list page.
        """
        return PageBlock.objects.filter(nested_block=self, publish=True)

    def is_published(self):
        return self.publish

    is_published.admin_order_field = 'publish'
    is_published.boolean = True
    is_published.short_description = _(u'Опубликовано?')


class Slider(models.Model):
    TYPES = (
        (0, _(u'Обычный')),
        (1, _(u'Отзывы')),
    )
    type_slider = models.IntegerField(
        _(u'Тип слайдера'),
        choices=TYPES,
        blank=True,
        null=True
    )
    name = models.CharField(_(u'Название'), max_length=50)
    page_block = models.ForeignKey(
        PageBlock,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _(u'Слайдер')
        verbose_name_plural = _(u'Слайдер')


class SliderItem(models.Model):
    title = models.CharField(
        _(u'Заголовок'),
        max_length=100,
        blank=True,
        null=True
    )
    text = RichTextField(
        _(u'Текст'),
        blank=True,
        null=True
    )
    publish = models.BooleanField(_(u'Публиковать'), default=False)
    slider = models.ForeignKey(
        to='pages.Slider',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_(u'Слайдер')
    )
    position = models.PositiveIntegerField(
        _(u'Позиция'),
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['position']
        verbose_name = _(u'Елемент слайдера')
        verbose_name_plural = _(u'Елементы слайдера')

    def is_published(self):
        return self.publish

    is_published.admin_order_field = 'publish'
    is_published.boolean = True
    is_published.short_description = _(u'Опубликовано?')

    def __str__(self):
        return f'SliderItem {self.title}'


class News(models.Model):
    title = models.CharField(
        _(u'Заголовок'),
        max_length=250,
    )
    text = RichTextField(_(u'Текст'))
    image = models.ImageField(
        _(u'Изображение'),
        upload_to=image_path,
        blank=True,
        null=True
    )
    show_more_button = models.BooleanField(
        _(u'Показывать кнопку перехода'),
        default=False
    )
    button_text = models.CharField(
        _(u'Текст кнопки'),
        max_length=50,
        default=_(u'Узнать больше'),
        blank=True,
        null=True
    )
    button_link = models.URLField(
        _(u'Ссылка кнопки'),
        blank=True,
        null=True
    )
    page_block = models.ForeignKey(
        PageBlock,
        on_delete=models.SET_NULL,
        verbose_name=_(u'Блок страницы'),
        blank=True,
        null=True
    )
    publish = models.BooleanField(_(u'Публивовать'), default=False)
    created = models.DateTimeField(_(u'Создано'), auto_now_add=True)
    updated = models.DateTimeField(_(u'Обновлено'), auto_now=True)
    position = models.PositiveIntegerField(
        _(u'Позиция'),
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['position']
        verbose_name = _(u'Новость')
        verbose_name_plural = _(u'Новости')

    def is_published(self):
        return self.publish

    is_published.admin_order_field = 'publish'
    is_published.boolean = True
    is_published.short_description = _(u'Опубликовано?')


class Vacancy(models.Model):
    # title = RichTextField(
    #     _(u'Заголовок (название вакансии)')
    # )
    description = RichTextField(_(u'Описание'))
    publish = models.BooleanField(
        _(u'Публиковать'),
        default=False
    )
    created = models.DateTimeField(_(u'Создано'), auto_now_add=True)
    page_block = models.ForeignKey(
        to=PageBlock,
        on_delete=models.CASCADE,
    )
    position = models.PositiveIntegerField(
        _(u'Позиция'),
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['position']
        verbose_name = _(u'Вакансия')
        verbose_name_plural = _(u'Вакансии')

    def is_published(self):
        return self.publish

    is_published.admin_order_field = 'publish'
    is_published.boolean = True
    is_published.short_description = _(u'Опубликовано?')


class Review(models.Model):
    first_name = models.CharField(
        _(u'Имя'),
        max_length=50,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        _(u'Фамилия'),
        max_length=50,
        blank=True,
        null=True
    )
    company = models.CharField(
        _(u'Компания, или должность (краткое описание)'),
        max_length=250,
        blank=True,
        null=True
    )
    image = models.ImageField(
        _(u'Изображение'),
        upload_to=image_path,
        blank=True,
        null=True
    )
    text = RichTextField(
        _(u'Текст отзыва')
    )
    slider = models.ForeignKey(
        to=Slider,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    publish = models.BooleanField(
        _(u'Публиковать'),
        default=False
    )
    created = models.DateTimeField(auto_now_add=True)
    position = models.PositiveIntegerField(
        _(u'Позиция'),
        default=0,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['position']
        verbose_name = _(u'Отзыв')
        verbose_name_plural = _(u'Отзывы')

    def is_published(self):
        return self.publish

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    is_published.admin_order_field = 'publish'
    is_published.boolean = True
    is_published.short_description = _(u'Опубликовано?')
