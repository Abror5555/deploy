from django.db import models

# Create your models here.

class ContactTitle(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Sayt sarlavhasi")


class ContactBody(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Saytni so'rovnomasi")
    body = models.CharField(max_length=255, blank=True, null=True, verbose_name="So'rovnoma haqida")
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name="Telefon sarlavhasi")
    number = models.CharField(max_length=255, blank=True, null=True, default="+998 93 1410111", verbose_name="Telefon raqam")
    number_link = models.CharField(max_length=500, blank=True, null=True, default="tel:+998931410111", verbose_name="Telefon link")
    office = models.CharField(max_length=255, blank=True, null=True, verbose_name="Office sarlavhasi")
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name="Office joylashuvi")
    office_link = models.CharField(max_length=5000, blank=True, null=True, verbose_name="location link", default="https://www.google.com/maps/place/Jondor+tuman+hokimligi/@39.7441366,64.1652202,2620m/data=!3m1!1e3!4m13!1m7!3m6!1s0x3f5aa5137d7b2901:0x2e75b5ab9ac3005!2z0JbQvtC90LTQvtGALCDQo9C30LHQtdC60LjRgdGC0LDQvQ!3b1!8m2!3d39.7425904!4d64.1744425!3m4!1s0x3f5aa5a361852f17:0x242aec5674b2621a!8m2!3d39.7399073!4d64.1864513")
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email adress")
    Email_address = models.CharField(max_length=255, blank=True, null=True, default="abrorkushshiyev@gmail.com", verbose_name="Email silkasi")
    email_link = models.CharField(max_length=500, blank=True, null=True, default="mailto:abrorkushshiyev@gmail.com", verbose_name="Email link")
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name="Website")
    website_address = models.CharField(max_length=255, blank=True, null=True, default="abrorbek.com", verbose_name="Wesite silkasi")
    website_link = models.CharField(max_length=255, blank=True, null=True, default="https://abrorbek.com", verbose_name="Wesite link")
    
    # UZB VS ENG INPUT

    send_email = models.CharField(max_length=300, blank=True, null=True, verbose_name="Xabar yuborish bo'limi")
    message = models.CharField(max_length=300, blank=True, null=True, verbose_name="Email yuborish izohi")
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name="Input shaxs nomi nomi")
    email_send = models.CharField(max_length=200, blank=True, null=True, verbose_name="Input email nomi")
    subject = models.CharField(max_length=200, blank=True, null=True, verbose_name="Input subject nomi")
    message_send = models.CharField(max_length=200, blank=True, null=True, verbose_name="Input message nomi")
    send_message = models.CharField(max_length=200, blank=True, null=True, verbose_name="Input Send Message nomi")

    def __str__(self) -> str:
        return self.title

    
    


class Contact(models.Model):
    name = models.CharField(max_length=155, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    


class ContactComplite(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ma'lumot olnigani haqida xabar berish")
    body = models.CharField(max_length=255, blank=True, null=True, verbose_name="Olingan ma'lumot haqida xabar berish")

    def __str__(self) -> str:
        return self.title