from modeltranslation.translator import TranslationOptions, register
from contact.models import ContactTitle, ContactBody, ContactComplite

@register(ContactTitle)
class ContactTitleTranslationOptions(TranslationOptions):
    fields = ('title',)



@register(ContactBody)
class ContactBodyTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'phone', 'office', 'location', 'email', 'website',
        'send_email', 'message', 'name', 'email_send', 'subject', 'message_send', 'send_message')



@register(ContactComplite)
class ContactCompliteTranslationOptions(TranslationOptions):
    fields = ('title', 'body')