from django.urls import path

from .views import *

urlpatterns = [
    path('books/', GetCreateBooksListView.as_view(), name='books'),
    path('books/<int:pk>', UpdateDeleteBooksListView.as_view(), name='books'),
]