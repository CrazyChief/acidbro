# -*- coding: utf-8 -*-
from django.contrib import admin

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from modeltranslation.admin import (
    TranslationAdmin, TranslationTabularInline, TranslationStackedInline,
    TabbedTranslationAdmin
)

from .models import (
    SiteSettings, FooterSettings, NavigationMenu, NavigationLinks
)


class HeaderSettingsAdminMixin(object):
    """
    Mixin класс для разделения сео данных в админ панели
    """
    def get_fieldsets(self, request, obj=None):
        seo_fields = ['left_side_title_en', 'left_side_title_ru',
                      'right_side_title_en', 'right_side_title_ru',
                      'right_side_description_en', 'right_side_description_ru',
                      'button_text_en', 'button_text_ru',
                      'button_link_en', 'button_link_ru']
        if self.fieldsets:
            return self.fieldsets
        fields = [
            x for x in self.get_fields(request, obj) if not x in seo_fields
        ]
        return [
            (None, {'fields': fields}), ('HeaderSettings', {
                'fields': seo_fields
            })
        ]


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fields = ('favicon', 'logo')


@admin.register(FooterSettings)
class FooterSettingsAdmin(TabbedTranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class NavigationLinksTabularInline(
        SortableInlineAdminMixin, TranslationStackedInline):
    model = NavigationLinks
    extra = 0


@admin.register(NavigationMenu)
class NavigationMenuAdmin(TabbedTranslationAdmin):
    list_display = ['name', 'menu_type']
    inlines = (NavigationLinksTabularInline,)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
            'js/admin/admin_navigation_menu.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
