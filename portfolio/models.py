from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Portfolio_Category(models.Model):
    title = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name="Portfolio Categorya nomi")
    body = models.CharField(max_length=500, null=True, blank=True, verbose_name="Portfolio Categoryasi haqida qisqa ma'lumot")
    image = models.ImageField(upload_to='portfolio/category', null=True, blank=True, verbose_name="Portfolio Categoryasi rasmi")
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('projects_by_portfolio', args=[self.slug])


class PortfolioCount(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Portfel haqida")
    projects = models.CharField(max_length=300, null=True, blank=True, verbose_name="Mening oxirgi loyihalarim")

    def __str__(self) -> str:
        return self.title



class Portfolio_Project(models.Model):
    title = models.CharField(max_length=255, unique=True, null=True, blank=True, verbose_name="Proyekt nomi")
    slug = models.SlugField(max_length=255, unique=True)
    body = models.CharField(max_length=500, null=True, blank=True, verbose_name="Proyekt haqida ma'lumot")
    category = models.ForeignKey(Portfolio_Category, on_delete=models.CASCADE, verbose_name="Proyekt Categoriyasi")
    image = models.ImageField(upload_to='portfolio/rest-framework', verbose_name="Proyekt rasmi")
    # DASTUR ISHALOV JARAYONIDA BO'LSA
    is_available = models.BooleanField(default=True, verbose_name="Proyektga ishlov berish")
    created_ad = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=500, blank=True, null=True, verbose_name="Proyekt kod link")
    site_link = models.CharField(max_length=500, blank=True, null=True, verbose_name="Proyekt link")
    button = models.CharField(max_length=200, blank=True, null=True, verbose_name="Sayt kodi")
    button1 = models.CharField(max_length=200, blank=True, null=True, verbose_name="Saytni ko'rish")
    created_time = models.CharField(max_length=255, blank=True, null=True, verbose_name="Yartilgan vaqat")
    
    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('portfolio_detail', args=[self.category.slug, self.slug])




class HitCount(models.Model):
    hit_count = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    