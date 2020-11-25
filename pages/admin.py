from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from modeltranslation.admin import (
    TranslationAdmin, TranslationTabularInline, TranslationStackedInline,
    TabbedTranslationAdmin
)

from core.admin import HeaderSettingsAdminMixin, NavigationLinksTabularInline
from seo.admin import SeoAdminMixin

from .models import (
    Page, PageBlock, Slider, SliderItem, News, Vacancy, Review
)


class PageBlockStackedInline(
        SortableInlineAdminMixin, TranslationStackedInline):
    model = PageBlock
    extra = 0
    fields = (
        'block_type', 'title', 'title_color', 'publish'
    )
    show_change_link = True


class PageBlockStackedInlineExtended(
        SortableInlineAdminMixin, TranslationStackedInline):
    model = PageBlock
    extra = 0
    fields = (
        'block_type', 'title', 'title_color', 'text', 'publish'
    )
    show_change_link = True


class SliderItemTabularInline(
        SortableInlineAdminMixin, TranslationStackedInline):
    model = SliderItem
    extra = 0
    fields = ('title', 'text', 'publish', 'position')


class SliderTabularInline(TranslationStackedInline):
    model = Slider
    extra = 0
    fields = ('type_slider', 'name')
    show_change_link = True


class NewsStackedInline(
        SortableInlineAdminMixin, TranslationStackedInline):
    model = News
    extra = 0
    fields = (
        'title', 'image', 'text', 'show_more_button', 'button_text',
        'button_link', 'publish', 'position'
    )
    show_change_link = True


class VacancyStackedInline(SortableInlineAdminMixin, TranslationStackedInline):
    model = Vacancy
    extra = 0
    fields = ('description', 'position', 'publish')
    show_change_link = True


class ReviewStackedInline(SortableInlineAdminMixin, TranslationStackedInline):
    model = Review
    extra = 0
    fields = (
        'first_name', 'last_name', 'company', 'text',
        'image', 'publish', 'position'
    )
    show_change_link = True


@admin.register(Vacancy)
class VacancyAdmin(TabbedTranslationAdmin):
    list_display = ['page_block', 'is_published']


@admin.register(Review)
class ReviewAdmin(TabbedTranslationAdmin):
    list_display = [
        'first_name', 'last_name', 'is_published'
    ]


@admin.register(Slider)
class SliderAdmin(TabbedTranslationAdmin):
    list_display = ['type_slider', 'name', 'page_block']
    inlines = (SliderItemTabularInline, ReviewStackedInline)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
            'js/admin/admin_slider.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(PageBlock)
class PageBlockAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    list_display = ['block_type', 'page_object', 'title', 'is_published']
    fields = (
        'block_type', 'page_object', 'title', 'title_color', 'subtitle',
        'text', 'background_image', 'use_slider', 'publish'
    )
    inlines = (
        PageBlockStackedInlineExtended,
        NavigationLinksTabularInline,
        SliderTabularInline,
        NewsStackedInline,
        VacancyStackedInline
    )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
            'js/admin/admin_page_block.js',
            'js/admin/admin_content_helper.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Page)
class PageAdmin(SortableAdminMixin, TabbedTranslationAdmin):
    list_display = ['name', 'template', 'is_published']
    prepopulated_fields = {"slug": ("name",)}

    inlines = (PageBlockStackedInline,)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
            'js/admin/admin_page.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


