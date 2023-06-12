from django.db import models
import os
def file_path(instace,filename):
    path = "documents/"
    format = 'uploaded-' + filename
    return os.path.join(path,format)

# Create your models here.

class DownloadFile(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Download rezume title")

class FileHandler(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Reyzumi ni Tili va nomi")
    btn = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tugma tili")
    file_upload = models.FileField(upload_to=file_path)

    def __str__(self) -> str:
        return str(self.file_upload)