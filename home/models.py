from django.db import models

# Create your models here.


class MenuPage(models.Model):
    a = models.CharField(max_length=200, blank=True, null=True, verbose_name="Sayt bosh harfi")
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sayt sarlavhasi")
    home = models.CharField(max_length=200, blank=True, null=True, verbose_name="sayt menu_bar home-page bo'limi")
    about = models.CharField(max_length=200, blank=True, null=True, verbose_name="sayt menu_bar about bo'limi")
    services = models.CharField(max_length=200, blank=True, null=True, verbose_name="sayt menu_bar servis bo'limi")
    portfolio = models.CharField(max_length=200, blank=True, null=True, verbose_name="sayt menu_bar portfolio bo'limi")
    contact = models.CharField(max_length=200, blank=True, null=True, verbose_name="sayt menu_bar contact bo'limi")
    color = models.CharField(max_length=500, blank=True, null=True, verbose_name="Sayt temasi")

    def __str__(self) -> str:
        return self.a





class HomePage(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, verbose_name="Sayt sarlavhasi")
    name = models.CharField(max_length=300, null=True, blank=True, verbose_name="Ism sharf")
    work = models.CharField(max_length=255, null=True, blank=True, verbose_name="ish bilan tanishtirish")
    work_title = models.CharField(max_length=300, blank=True, null=True, verbose_name="Ish nomi")
    body = models.CharField(max_length=800, blank=True, null=True, verbose_name="Men haqimda qisqa ma'lumot")
    image = models.ImageField(upload_to='home/')
    download = models.CharField(max_length=255, null=True, blank=True, verbose_name="Download CV")

    def __str__(self) -> str:
        return self.title




class Range(models.Model):
    color_1 = models.CharField(max_length=255, blank=True, null=True)
    color_2 = models.CharField(max_length=255, blank=True, null=True)
    color_3 = models.CharField(max_length = 255, blank=True, null=True)
    color_4 = models.CharField(max_length = 255, blank=True, null=True)
    color_5 = models.CharField(max_length = 255, blank=True, null=True)
    color_6 = models.CharField(max_length = 255, blank=True, null=True)   