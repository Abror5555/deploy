from django.contrib import admin
from download.models import DownloadFile, FileHandler

# Register your models here.

admin.site.register(DownloadFile)
admin.site.register(FileHandler)