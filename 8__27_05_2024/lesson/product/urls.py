from django.urls import path
from .views import index, store, add_categ, change_categ

urlpatterns = [
    path('', index, name='index'),
    path('store/<int:store_id>', store, name='store'),
    path('add', add_categ, name='add'),
    path('change_categ/<int:categ_id>', change_categ, name='change_categ')
]