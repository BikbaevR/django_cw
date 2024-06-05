from django.shortcuts import render, redirect
from .models import Book


# Create your views here.


def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'library/index.html', context)



def add_book(request):
    if(request.method == 'POST'):
        book = Book()
        book.name = request.POST['book_name']
        book.image = request.FILES['book_image']
        book.save()


    return redirect('index')


def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('index')