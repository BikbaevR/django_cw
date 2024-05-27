from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.text import slugify

from .models import Store, Category


# Create your views here.

def index(request):
    search = request.GET.get('search') or ''
    shops = Store.objects.filter(name__icontains=search)

    return render(request, 'product/index.html', context={'shops': shops})


def store(request, store_id):
    category = Category.objects.all()

    return redirect(request, 'product/store/html', context={'category': category})
