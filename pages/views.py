import os

from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseNotFound

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
        print('\n\n\nDEBUG:')
        self.pieces = [
            x for x in request.META["PATH_INFO"].split('/')
            if x != ''
        ]
        self.pieces.pop(0)
        print(self.pieces)
        if len(self.pieces) == 0:
            try:
                self.object = Page.objects.get(
                    template__exact=0, publish=True)
            except ObjectDoesNotExist:
                self.object = None
        else:
            try:
                self.object = Page.objects.get(
                    slug__exact=self.pieces[0], publish=True)
            except ObjectDoesNotExist:
                return HttpResponseNotFound(
                    'Oooops, page you a looking for does not exist!')
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        # context['menu'] = self.get_menu()
        pprint(context)
        return context


# class AboutView(TemplateView):
#
#     template_name = 'about.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['object'] = self.get_page(1)
#         return context
#
#
# class ContactView(TemplateView):
#
#     template_name = 'contact.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['object'] = self.get_page(2)
#         return context
#
#
# class NewsView(TemplateView):
#
#     template_name = 'news.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['object'] = self.get_page(3)
#         return context
#
#
# class PortfolioView(TemplateView):
#
#     template_name = 'portfolio.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['object'] = self.get_page(4)
#         return context
#
#
# class VacanciesView(TemplateView):
#
#     template_name = 'vacancies.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['object'] = self.get_page(0)
#         return context
