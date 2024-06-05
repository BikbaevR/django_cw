from django.urls import path
from .views import index, add_book, delete

urlpatterns = [
    path('', index, name='index'),
    path('add_book', add_book, name='add_book'),
    path('book/<int:id>/', delete, name='delete'),
]