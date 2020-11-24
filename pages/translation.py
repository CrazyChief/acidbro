from modeltranslation.translator import register, TranslationOptions

from .models import (
    Page, PageBlock, Slider, SliderItem, News, Vacancy, Review
)


@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'page_title', 'page_keywords', 'page_description',
              'left_side_title', 'right_side_title', 'right_side_description',
              'button_text')


@register(PageBlock)
class PageBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(Slider)
class SliderTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(SliderItem)
class SliderItemTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'button_text')


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'company', 'text')
