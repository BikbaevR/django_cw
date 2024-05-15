from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'post/index.html')


def about(request):
    return render(request, 'post/about.html')


def contact(request):
    return render(request, 'post/contact.html')
