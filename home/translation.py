from modeltranslation.translator import TranslationOptions, register
from home.models import MenuPage, HomePage

@register(MenuPage)
class MenuPageTranslationOptions(TranslationOptions):
    fields = ('home', 'about', 'services', 'portfolio', 'contact', 'color')



@register(HomePage)
class HomePageTranslationOptions(TranslationOptions):
    fields = ('title', 'name', 'work', 'work_title', 'body', 'download')