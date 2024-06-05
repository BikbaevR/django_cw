from django.shortcuts import render, redirect
from .models import *


# from PIL #для работы с картинками

# Create your views here.


def index(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()

    context = {'books': books, 'categories': categories, 'authors': authors}
    return render(request, 'library/index.html', context)



def add_book(request):
    if request.method == 'POST':
        book = Book()
        book.name = request.POST['book_name']
        book.image = request.FILES['book_image']
        book.save()


    return redirect('index')


def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('index')



def category(request, id):
    category = Category.objects.get(pk=id)
    books = Book.objects.filter(category=category)

    categories = Category.objects.all()
    authors = Author.objects.all()

    context = {'books': books, 'categories': categories, 'authors': authors, 'category': category}
    return render(request, 'library/category.html', context)


def author(request, id):
    author = Author.objects.get(pk=id)
    books = Book.objects.filter(author=author)

    categories = Category.objects.all()
    authors = Author.objects.all()

    context = {'books': books, 'categories': categories, 'authors': authors, 'author': author}
    return render(request, 'library/author.html', context)


def add_categ_view(request):
    return render(request, 'library/add_categ.html')


def add_categ(request):
    if request.method == 'POST':
        category = Category()
        category.name = request.POST.get('category_name')
        category.image = request.FILES['category_img']
        category.save()
        return redirect('index')