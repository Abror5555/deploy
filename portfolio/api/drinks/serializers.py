from rest_framework import serializers
from portfolio.api.drinks.models import Drink

class DirnkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']