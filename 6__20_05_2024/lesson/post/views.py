from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post
# Create your views here.


def index(request):

    print('hello')

    cat = Category.objects.get(pk=1)
    # cat = Category.objects.get(pk__gte=2)

    print(cat)


    # post = Post(
    #     title='title 1',
    #     category=cat
    # )
    # print(post)


    return HttpResponse("success")