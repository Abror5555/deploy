from django.shortcuts import render
from services.models import ServicesTitile, ServicesModel

# Create your views here.

def services(request):
    title = ServicesTitile.objects.all()
    services = ServicesModel.objects.all()

    context = {
        'title': title,
        'services': services
    }

    return render(request, 'ser/services.html', context)