from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django import forms

# Create your views here.

from app.forms import PostForm, UsersForm


def index(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
        else:
            # print(form.errors)
            ...


    cntx = {'form': form}

    return render(request, 'app/index.html', cntx)



def users(request):
    form = UsersForm()

    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            form = UsersForm()

    cntx = {'form': form}
    return render(request, 'app/users.html', cntx)