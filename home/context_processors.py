from home.models import MenuPage, Range

def menu_bar(request):
    menu_bar_category = MenuPage.objects.all()
    return {"menu_bar": menu_bar_category}



def range(request):
    range = Range.objects.all()
    return {"range": range}