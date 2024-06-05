from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_book', add_book, name='add_book'),
    path('book/<int:id>/', delete, name='delete'),
    path('category/<int:id>', category, name='category'),
    path('author/<int:id>', author, name='author'),
    path('add_categ_view', add_categ_view, name='add_categ_view'),
    path('add_categ', add_categ, name='add_categ'),
]