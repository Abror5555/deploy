from django.urls import path
from portfolio.api.drinks.views import drink_list, drinks_detail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('drinks/', drink_list, name='drink'),
    path('drinks/<int:id>', drinks_detail, name='drink_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)