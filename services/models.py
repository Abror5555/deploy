from django.db import models

# Create your models here.

class ServicesTitile(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Sayt sarlavhasi")

    def __str__(self) -> str:
        return self.title



class ServicesModel(models.Model):
    image = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name="Servis nomi")
    body = models.CharField(max_length=600, blank=True, null=True, verbose_name="Servis ma'lumoti")

    def __str__(self) -> str:
        return self.title