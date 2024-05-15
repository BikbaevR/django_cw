from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all()

    # Post.objects.get(pk = 1).delete()

    return render(request, 'post/index.html', context={'posts': posts})


def about(request):
    return render(request, 'post/about.html')


def contact(request):
    return render(request, 'post/contact.html')


def publication(request):
    return HttpResponse('')
