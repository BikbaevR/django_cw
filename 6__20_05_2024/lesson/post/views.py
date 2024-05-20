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

    # post = Post.objects.get(pk=1)
    # post.description = 'TEST'
    # post.content = 'TEEEEEEEEEEEEEST'
    # post.save()

    # post, _ = Post.objects.get_or_create(title="title new", category=cat)
    # post, _ = Post.objects.get_or_create(title="title new2", defaults={
    #     "category": cat,
    #     'description': 'eeeeeeeeeeeeeeeeeeeeeeee'
    # })

    # post, _ = Post.objects.update_or_create(title='title new', defaults={
    #     "content": 'sssssssssssssss',
    #     'is_published': True
    # })
    #
    # print(post)
    # post.description = 'asdasdasdasdsa'
    # post.save()

    data1 = [
        {
            'title': 'title25',
            'category': cat,
        }
    ]



    # data = [
    #     Post(title='title6', category=cat),
    #     Post(title='title7', category=cat),
    #     Post(title='title8', category=cat),
    #     Post(title='title9', category=cat),
    # ]

    data = list(map(lambda i: Post(**i), data1))

    Post.objects.bulk_create(data)

    return HttpResponse("success")
