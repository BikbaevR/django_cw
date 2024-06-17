from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Post, Comments


def index(request):
    categoryes = Category.objects.all()
    posts = Post.objects.all()
    cntx = {
        'categoryes': categoryes,
        'posts': posts
    }

    return render(request, 'cw/index.html', context=cntx)


def categories(request):
    categ = Category.objects.all()

    return render(request, 'cw/categoryes.html', context={'categ': categ})


def category(request, id):

    posts = Post.objects.filter(category=Category.objects.get(pk=id))

    categ = Category.objects.get(pk=id)

    return render(request, 'cw/category.html', context={'posts': posts, 'category': categ})


def post(request, id):
    post = Post.objects.get(pk=id)
    comments = Comments.objects.filter(post=post)

    cntx = {
        "post": post,
        "comments": comments
    }

    return render(request, 'cw/details.html', context=cntx)


def add_category(request):
    categ_name = request.POST.get('categ_name')
    if categ_name:
        categ = Category(name=categ_name)
        categ.save()
        return redirect('categories')


def add_post(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')

    # print(f"{title} {description} {category}")

    post = Post()
    post.title = title
    post.description = description

    post.category = Category.objects.get(pk=category)
    post.save()

    return redirect('index')


def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('index')


def change_post_view(request, id):
    post = Post.objects.get(pk=id)
    categoryes = Category.objects.all()

    # print('asdasdassad',post.description)

    cntx = {
        'post': post,
        'categoryes': categoryes
    }

    return render(request, 'cw/change_post.html', context=cntx)


def change_post(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')


    post = Post.objects.get(pk=id)

    post.title = title
    post.description = description
    post.category = Category.objects.get(pk=category)

    post.save()

    return redirect('index')


def add_comment(request):
    author = request.POST.get('author')
    comment_ = request.POST.get('comment')
    post_id = request.POST.get('id')
    print(post_id)

    com = Comments()
    com.author = author
    com.comment = comment_
    post = Post.objects.get(pk=post_id)

    com.post = post
    com.save()
    return redirect(request.META.get('HTTP_REFERER'))



def edit_category_name(request):
    categ_id = request.POST.get('categ_id')
    new_category_name = request.POST.get('new_categ_name')

    category = Category.objects.get(pk=categ_id)
    category.name = new_category_name
    category.save()

    return redirect(request.META.get('HTTP_REFERER'))



def delete_category(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('categories')


def delete_post_in_categ(request, id):
    category = Category.objects.get(pk=id)
    posts = Post.objects.filter(category=category)
    posts.delete()
    return redirect('categories')


