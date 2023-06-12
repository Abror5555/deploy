from modeltranslation.translator import TranslationOptions, register
from services.models import ServicesTitile, ServicesModel

@register(ServicesTitile)
class ServicesTitileTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ServicesModel)
class ServicesModelTranslationOptions(TranslationOptions):
    fields = ('title', 'body')