from django.contrib import admin
from tlgbot.my_bot.models import BotUser, FeedBack

# Register your models here.

# BOTUSER ADMIN
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'created_at']

admin.site.register(BotUser, BotUserAdmin)


# FEEDBACK ADMIN
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

admin.site.register(FeedBack, FeedBackAdmin)