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
    store = get_object_or_404(Store, pk=store_id)
    category = Category.objects.all()
    print(category)


    cntx = {
        'category': category,
        'store': store
    }

    return render(request, 'product/store.html', context=cntx)


def add_categ(request):
    categ_name = request.POST.get('store_name')
    print(categ_name)

    category = Category()
    category.name = categ_name
    category.slug = slugify(category.name)
    category.save()
    # return redirect('store', store_id=1)

    return redirect(request.META.get('HTTP_REFERER'))


def change_categ(request, categ_id):
    categ_ids = request.POST.get('categ_id')
    category = get_object_or_404(Category, pk=categ_ids)
    category.name = request.POST.get('new_categ_name')
    category.save()
    return redirect('index')