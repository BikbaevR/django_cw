from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_post', add_post, name='add_post'),
    path('delete/<int:id>', delete_post, name='delete_post'),
    path('change_post_view/<int:id>', change_post_view, name='change_post_view'),
    path('change_post', change_post, name='change_post'),
    path('post/<int:id>', post, name='post'),
    path('add_comment', add_comment, name='add_comment'),
    path('categories', categories, name='categories'),
    path('category/<int:id>', category, name='category'),
    path('add_category', add_category, name='add_category'),
    path('edit_category_name', edit_category_name, name='edit_category_name'),
    path('delete_category/<int:id>', delete_category, name='delete_category'),
    path('delete_post_in_categ/<int:id>', delete_post_in_categ, name='delete_post_in_categ'),

]