from django.shortcuts import render
from .models import Child, Kiosk


# Create your views here.


def index(request):

    childs = Child.objects.all()
    kiosk = Kiosk.objects.all()

    return render(request, 'index.html', context={'childs': childs, 'kiosk': kiosk})