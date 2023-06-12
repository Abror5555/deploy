from django.urls import path
from tlgbot.my_bot.views import BotUsersApiView, FeedbackApiView

urlpatterns = [
    path('bot-users/', BotUsersApiView.as_view(), name='bot-users'),
    path('feedback/', FeedbackApiView.as_view(), name='feedbacks'),
]