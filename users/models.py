from django.db import models
# from django.contrib.auth.models import AbstractUser
# from portfolio.shop.models import Product

# Create your models here.

# class CustomUser(AbstractUser):
#     phone_number = models.CharField(max_length=17)
#     tg_username = models.CharField(max_length=150)
#     avatar = models.ImageField(upload_to='avatars/' )# default='./media/avatars/default.png')
    
#     def __str__(self):
#         return str(self.username)
    
# class Saved(models.Model):
#     # product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)    
#     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)    
#     date  = models.DateField(auto_now_add=True)
    
#     def __str__(self):
#         return "Comment of " + str(self.author.username)    
