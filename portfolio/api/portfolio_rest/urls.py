from django.urls import path, include
from portfolio.api.portfolio_rest.views import ApiViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('filter', ApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
