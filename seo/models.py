from django.db import models
from django.utils.translation import ugettext_lazy as _


class SeoMeta(models.Model):
    """
    Абстрактный класс сео мета данных
    """
    page_title = models.CharField(
        _(u'Заголовок страницы (SEO/Meta)'),
        max_length=350,
        blank=True,
    )
    page_keywords = models.CharField(
        _(u'Ключевые слова страницы (SEO/Meta)'),
        max_length=500,
        blank=True
    )
    page_description = models.CharField(
        _(u'Описание страницы (SEO/Meta)'),
        max_length=1000,
        blank=True
    )

    class Meta:
        abstract = True

