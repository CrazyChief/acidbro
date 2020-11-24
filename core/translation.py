from modeltranslation.translator import register, TranslationOptions

from .models import FooterSettings, NavigationLinks, NavigationMenu


@register(FooterSettings)
class FooterSettingsTranslationOptions(TranslationOptions):
    fields = ('country', 'state', 'city', 'address_1', 'address_2',
              'text', 'copyright_text')


@register(NavigationLinks)
class NavigationLinksTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(NavigationMenu)
class NavigationMenuTranslationOptions(TranslationOptions):
    fields = ('name',)
