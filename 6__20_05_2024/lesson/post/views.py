from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post
from django.shortcuts import get_object_or_404


# Create your views here.


def index(request):
    print('hello')

    cat = Category.objects.get(pk=1)
    # cat = Category.objects.get(pk__gte=2)
    # cat = get_object_or_404(Category, name='asasdsad')

    print(cat)

    # post = Post(
    #     title='title 1',
    #     category=cat
    # )

    # post.save()

    # post = Post.objects.create(title='title 2', category=cat)
    # print(post)

    post = Post.objects.get(pk=1)
    post.description = 'TEST'
    post.content = 'TEEEEEEEEEEEEEST'
    post.save()

    return HttpResponse("success")