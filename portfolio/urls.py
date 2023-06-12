from django.urls import path, include
from portfolio.views import Portfolio_project_Views, Portfolio, Portfolio_detail


urlpatterns = [
    path('', Portfolio, name='portfolio'),
    path('<slug:category_slug>/', Portfolio_project_Views, name='projects_by_portfolio'),
    path('<slug:category_slug>/<slug:portfolio_slug>/', Portfolio_detail, name='portfolio_detail'),    
]
