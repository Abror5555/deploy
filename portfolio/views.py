from django.shortcuts import render, get_object_or_404
from portfolio.models import Portfolio_Category, Portfolio_Project
from portfolio.models import HitCount

from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

# Create your views here.

def Portfolio(request):
    return render(request, 'por/portfolio.html')



def Portfolio_project_Views(request, category_slug=None):
    if category_slug == None:
        rest = Portfolio_Project.objects.filter(is_available=True)
        
    else:
        categories = get_object_or_404(Portfolio_Category, slug=category_slug)
        rest = Portfolio_Project.objects.filter(is_available=True, category=categories)
    
    context = {
        'rest': rest,
        'rest_count': rest.count()
    }
    return render(request, 'por/portfolio_about.html', context)


def Portfolio_detail(request, category_slug, portfolio_slug):
    portfolio = get_object_or_404(Portfolio_Project, slug=portfolio_slug, category__slug=category_slug)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'por/portfolio_detail.html', context)


