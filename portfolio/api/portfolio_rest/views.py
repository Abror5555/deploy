from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from portfolio.api.portfolio_rest.models import PostFilter
from portfolio.api.portfolio_rest.serialzers import ApiFilterSerializers

# Create your views here.

class ApiViewSet(ModelViewSet):
    queryset = PostFilter.objects.all()
    serializer_class = ApiFilterSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','about']
