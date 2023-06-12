from django.db import models

# Create your models here.

class BotUser(models.Model):
    user_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)



class FeedBack(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self) -> str:
        return str(self.name)