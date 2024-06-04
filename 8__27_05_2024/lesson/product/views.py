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
    # print(category)


    cntx = {
        'category': category,
        'store': store
    }

    return render(request, 'product/store.html', context=cntx)


def add_categ(request):
    categ_name = request.POST.get('store_name')
    # print(categ_name)

    category = Category()
    category.name = categ_name
    category.slug = slugify(category.name)
    category.save()
    # return redirect('store', store_id=1)

    return redirect(request.META.get('HTTP_REFERER'))


def change_categ(request, categ_id):

    category = get_object_or_404(Category, pk=categ_id)
    category_id = categ_id

    cntx = {
        'category': category,
        'id': category_id
    }

    return render(request, 'product/change_categ.html', context=cntx)

def change_categ_confirm(request):

    category_id = request.POST.get('category_id')
    new_category_name = request.POST.get('category_name')

    print('aasdasds' + category_id)

    category = get_object_or_404(Category, pk=category_id)
    category.name = new_category_name
    category.save()

    return redirect('index')


def delete_categ(request, categ_id):
    category = get_object_or_404(Category, pk=categ_id)
    category.delete()
    return redirect('index')

def view_posts_categ(request, categ_id):
    posts =