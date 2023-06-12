from portfolio.models import Portfolio_Category, PortfolioCount

def menu_links(request):
    categories = Portfolio_Category.objects.all()
    return {"portfolio_categories": categories}


def portfel(request):
    categories = PortfolioCount.objects.all()
    return {"portfel": categories}