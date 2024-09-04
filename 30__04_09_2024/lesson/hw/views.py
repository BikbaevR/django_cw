from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serialize import *


class GetCreateBooksListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer




class UpdateDeleteBooksListView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer



