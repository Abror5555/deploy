from tlgbot.my_bot.models import BotUser, FeedBack
from rest_framework.serializers import ModelSerializer


class BotUserSerializer(ModelSerializer):
    class Meta:
        model = BotUser
        fields = ("name", "username", "user_id", "created_at")


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ("name", "user_id", "created_at", "body")