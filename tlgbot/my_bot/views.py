from django.shortcuts import render
from tlgbot.my_bot.models import BotUser, FeedBack
from tlgbot.my_bot.serializers import BotUserSerializer, FeedbackSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class BotUsersApiView(ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class FeedbackApiView(ListCreateAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedbackSerializer