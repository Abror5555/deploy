from modeltranslation.translator import TranslationOptions, register
from download.models import DownloadFile, FileHandler

@register(DownloadFile)
class DownloadFileTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FileHandler)
class FileHandlerTranslationOptions(TranslationOptions):
    fields = ('title', 'btn')