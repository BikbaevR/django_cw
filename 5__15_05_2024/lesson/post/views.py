from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Post, Category


# Create your views here.


def index(request):
    posts = Post.objects.all()

    # Post.objects.get(pk = 1).delete()
    # get_object_or_404(Post, title='asdas')

    return render(request, 'post/index.html', context={'posts': posts})


def about(request):
    return render(request, 'post/about.html')


def contact(request):
    return render(request, 'post/contact.html')


def publication(request, id: int):
    posts = Post.objects.get(pk=id)
    return render(request, 'post/post.html', context={'post': posts})


def delete_post(request, id: int):
    post = Post.objects.get(pk=id).delete()
    posts = Post.objects.all()

    # return render(request, 'post/index.html', context={'posts': posts})
    return redirect(index)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'post/category.html', context={'categories': categories})


def category_from_id(request, id: int):
    categories = Category.objects.get(pk=id)
    posts = Post.objects.filter(category=categories)
    return render(request, 'post/category_from_id.html', context={'posts': posts})
