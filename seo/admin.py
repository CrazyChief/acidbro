# -*- coding: utf-8 -*-


class SeoAdminMixin(object):
    """
    Mixin класс для разделения сео данных в админ панели
    """
    def get_fieldsets(self, request, obj=None):
        seo_fields = ['page_title_en', 'page_title_ru', 'page_keywords_en',
                      'page_keywords_ru', 'page_description_en',
                      'page_description_ru']
        if self.fieldsets:
            return self.fieldsets
        fields = [
            x for x in self.get_fields(request, obj) if not x in seo_fields
        ]
        return [
            (None, {'fields': fields}), ('SEO', {'fields': seo_fields})
        ]
