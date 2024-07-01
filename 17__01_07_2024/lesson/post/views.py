from django.shortcuts import render
from .models import *
from django.http import Http404


# Create your views here.

def index(request):
    page = int(request.GET.get('page') or 1)
    limit = 3

    posts = Post.objects.all()[(page - 1) * limit:page * limit:]

    if len(posts) == 0:
        raise Http404




    # for post in posts:
    #     post.title = f'{post.title} {post.pk}'
    #     post.save()

    # for i in range(10):
    #     Post.objects.create(
    #         title=posts[0].title,
    #         content=posts[0].content,
    #         images=posts[0].images,
    #         video_content=posts[0].video_content,
    #         audio_content=posts[0].audio_content,
    #         author=posts[0].author
    #     )
    context = {'posts': posts, 'next_page': page + 1, 'prev_page': page - 1 if page > 1 else 1}
    return render(request, 'post/index.html', context)
