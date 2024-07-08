from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('class/', IndexView.as_view(), name='index_class'),
    path('template_view/', IndexView2.as_view(), name='index_class_2'),
    path('list/', PostListView.as_view(), name='post_list'),
    path('post/<int:post_id>', PostDeatilView.as_view(), name='post_detail'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:post_id>/update', PostUpdateView.as_view(), name='post_update'),
]