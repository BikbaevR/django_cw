from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Post, Category

def index(request):

    # posts = Post.objects.filter(post_is_active=True, status = 'n')
    #
    # category = Category.objects.get(pk=1)
    #
    #
    # print(Post.objects.filter(category=category))
    # print(category.posts.all())
    # # print(category.post_set.all())
    #
    # # print(Post.objects.filter(category__name='текст')) У которого поле равно...
    # Post.objects.filter(title__startswith='строка')
    # # Post.objects.filter(title__contains='строка')
    # # Post.objects.filter(title__icontains='строка')
    # # for post in posts:
    # #     print(post.title)
    # #     print(post.category.name)
    return HttpResponse('')

