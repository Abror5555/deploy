from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class PostFilter(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField()

    def __str__(self) -> str:
        return self.title



# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     url = models.URLField
#     create = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.title