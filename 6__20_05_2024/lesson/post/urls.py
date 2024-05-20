from django.urls import  path
from .views import index, posts, post_info

urlpatterns = [
    path('', posts, name='post'),
    path('post/<int:post_id>', post_info, name='post_info')
]