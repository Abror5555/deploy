from django.db import models

# Create your models here.


class AboutModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="About Sahifasi")
    name = models.CharField(max_length=500, blank=True, null=True, verbose_name="Ism Sharf")
    work_name = models.CharField(max_length=500, blank=True, null=True, verbose_name="Work name")
    body = models.CharField(max_length=800, blank=True,null=True, verbose_name="Men haqimda ma'lumot")

    def __str__(self) -> str:
        return self.title


class AboutInformation(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name="Sarlavha ")
    information = models.CharField(max_length=400, blank=True, null=True, verbose_name="Ma'lumot")

    def __str__(self) -> str:
        return self.title




class LearningModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="O'rgangan programma tili")
    witdh = models.CharField(max_length=100, null=True, blank=True, default='95%', verbose_name="O'rgangan proggramma % ")
    skill = models.CharField(max_length=100, blank=True, null=True, default='95%', verbose_name="Foydalanuvchiga ko'rinadigan %")

    def __str__(self) -> str:
        return self.name

class HireMeModel(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True, verbose_name="Hire-Me")


class ExprementModel(models.Model):
    education = models.CharField(max_length=200, blank=True, null=True, verbose_name="o'qigan joylar")
    experience = models.CharField(max_length=200, blank=True, null=True, verbose_name="Amalyontalar qilingan ishlar")

    def __str__(self) -> str:
        return self.education


class EducationModel(models.Model):
    created = models.CharField(max_length=200, null=True, blank=True, verbose_name="Yaratilgan sana")
    title = models.CharField(max_length=555, null=True, blank=True, verbose_name="O'qigan joy nomi")
    body = models.CharField(max_length=1000, blank=True, null=True, verbose_name="O'qigan joydan ma'lumot")

    def __str__(self) -> str:
        return self.title



class ExperienceModel(models.Model):
    created = models.CharField(max_length=200, null=True, blank=True, verbose_name="Yaratilgan sana")
    title = models.CharField(max_length=555, null=True, blank=True, verbose_name="O'qigan joy nomi")
    body = models.CharField(max_length=1000, blank=True, null=True, verbose_name="O'qigan joydan ma'lumot")

    def __str__(self) -> str:
        return self.title