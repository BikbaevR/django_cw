from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import PostForm
from .models import *

def index(request):
    form = PostForm()
    if request.user.is_authenticated:
        # posts = Post.objects.filter(author=request.user)
        posts = request.user.posts.all()
    else:
        posts = Post.objects.all()

    cntx = {'form': form, 'posts': posts}

    return render(request, 'post/index.html', cntx)


@login_required(login_url='login')
# @requrie_POST
def add_post(request):
    form = PostForm(request.POST, request.FILES)
    print('1')
    if form.is_valid():
        print('2')
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('index')
    return redirect('index')