from rest_framework import serializers
from portfolio.api.portfolio_rest.models import PostFilter

class ApiFilterSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostFilter
        fields = ['title', 'about']