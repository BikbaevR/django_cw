from django.urls import path
from .views import index, store

urlpatterns = [
    path('', index, name='index'),
    path('store/<int:store_id>', store, name='store')
]