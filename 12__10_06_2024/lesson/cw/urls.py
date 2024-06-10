from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('posts/', posts, name='posts'),
    path('add_category', add_category, name='add_category'),
    path('list_category', list_category, name='list_category'),
]