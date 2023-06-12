from django.shortcuts import render
from home.models import HomePage

# Create your views here.

def home(request):
    site = HomePage.objects.all()
    context = {
        'site': site
    }
    return render(request, 'home.html', context)