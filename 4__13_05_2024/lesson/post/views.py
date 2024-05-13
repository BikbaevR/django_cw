from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post

def index(request):

    posts = Post.objects.all()

    for post in posts:
        print(post.title)
        print(post.category.name)

    return HttpResponse('')