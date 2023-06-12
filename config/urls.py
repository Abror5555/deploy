"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('portfolio/api/', include('portfolio.api.portfolio_rest.urls')),
    path('portfolio/api/', include('portfolio.api.drinks.urls')),
    path('', include('portfolio.videochat.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('api/users/', include('tlgbot.my_bot.urls')),
    # path('shop/', include('portfolio.shop.urls')),
    # path('users/', include("users.urls")),
    path('users/', include('django.contrib.auth.urls')),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('contact/', include('contact.urls')),
    path('home/', include('download.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)