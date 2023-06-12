from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from download.models import DownloadFile, FileHandler

# Create your views here.
class IndexView(TemplateView):
    template_name = 'download/down.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_files = FileHandler.objects.all
        down = DownloadFile.objects.all

        context = {'get_files': get_files, 'down': down}
        return context