from django.urls import path
from download.views import IndexView

urlpatterns = [
    path('download/', IndexView.as_view(), name='download_file'),
]
