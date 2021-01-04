import os

from django.conf import settings
from django.core import paginator
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseNotFound, Http404, HttpResponseRedirect

from core.models import (
    HeaderSettings, FooterSettings, SiteSettings, NavigationMenu,
    NavigationLinks
)

from .models import Page, PageBlock, Slider, SliderItem, News, Vacancy, Review

from pprint import pprint


class TemplateAdminAJAXView(TemplateView):
    template_part = None

    def get(self, request, *args, **kwargs):
        self.template_part = self.kwargs['text']
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        template = f'{self.template_part}_item.html'
        template_file = os.path.join(
            settings.PAGE_UPLOAD_TEMPLATE, f'{template}')
        try:
            with open(template_file, 'r') as f:
                context['template'] = f.read()
        except FileNotFoundError:
            pass
        return context

    def render_to_response(self, context, **response_kwargs):
        html = context['template']
        return JsonResponse({
            'html': html
        }, safe=False, **response_kwargs)


class MenuMixin(object):

    def get_menu(self):
        try:
            menu = NavigationMenu.objects.get(menu_type=0)
        except ObjectDoesNotExist:
            menu = None
        except MultipleObjectsReturned:
            menu = None

        return menu

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = self.get_menu()
    #     return context


class SettingsMixin(object):
    footer = None

    def get_site_settings(self):
        try:
            site_settings = SiteSettings.objects.first()
        except ObjectDoesNotExist:
            site_settings = None

        return site_settings

    def get_footer(self):
        try:
            self.footer = FooterSettings.objects.first()
        except ObjectDoesNotExist:
            self.footer = None

        return self.footer

    def get_footer_menu(self):
        footer_menu = None

        if self.footer:
            try:
                pprint(self.footer.footer_menus)
                footer_menu = self.footer.footer_menus.filter(
                    menu_type=1).first()
            except ObjectDoesNotExist:
                footer_menu = None

        return footer_menu

    def get_footer_social_menu(self):
        footer_social_menu = None

        if self.footer:
            try:
                footer_social_menu = self.footer.footer_menus.filter(
                    menu_type=2).first()
            except ObjectDoesNotExist:
                footer_social_menu = None

        return footer_social_menu

    def get_footer_contact_menu(self):
        footer_contact_menu = None

        if self.footer:
            try:
                footer_contact_menu = self.footer.footer_menus.filter(
                    menu_type=3).first()
            except ObjectDoesNotExist:
                footer_contact_menu = None

        return footer_contact_menu


class PageMixin(TemplateView, MenuMixin, SettingsMixin):

    def __init__(self):
        super().__init__()
        self.pieces = None
        self.object = None
        self.object_type = None

    def get(self, request, *args, **kwargs):
        self.pieces = [
            x for x in request.META["PATH_INFO"].split('/')
            if x != ''
        ]
        self.pieces.pop(0)
        if len(self.pieces) == 0:
            try:
                self.object = Page.objects.get(
                    template__exact=0, publish=True)
            except ObjectDoesNotExist:
                self.object = Page.objects.get(
                    template__exact=6)
                return HttpResponseRedirect(self.object.get_absolute_url())
        else:
            try:
                self.object = Page.objects.get(
                    slug__exact=self.pieces[0], publish=True)
            except ObjectDoesNotExist:
                self.object = Page.objects.get(
                    template__exact=6)
                return HttpResponseRedirect(self.object.get_absolute_url())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = self.get_menu()
        context['site_settings'] = self.get_site_settings()
        context['footer_settings'] = self.get_footer()
        context['footer_menu'] = self.get_footer_menu()
        context['footer_social_menu'] = self.get_footer_social_menu()
        context['footer_phones'] = self.get_footer_contact_menu()
        return context


class IndexView(PageMixin):

    template_name = 'base.html'
    news_paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object

        if self.object.template == 3:
            news_page = self.request.GET.get('news_page')
            news_wrapper = self.object.pageblock_set.filter(
                block_type=1, publish=True).first()
            news = news_wrapper.news_set.published()
            news_paginator = paginator.Paginator(news, self.news_paginate_by)

            # Catch invalid page numbers
            try:
                news_page_obj = news_paginator.page(news_page)
            except (paginator.PageNotAnInteger, paginator.EmptyPage):
                news_page_obj = news_paginator.page(1)

            context["news_page_obj"] = news_page_obj

        return context

