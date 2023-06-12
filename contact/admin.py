from django.contrib import admin
from contact.models import Contact, ContactTitle, ContactBody, ContactComplite

# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactTitle)
admin.site.register(ContactBody)
admin.site.register(ContactComplite)