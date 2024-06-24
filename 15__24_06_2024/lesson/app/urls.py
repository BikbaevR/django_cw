from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('post/create', create, name='create'),
    path('users', users, name='users'),
]