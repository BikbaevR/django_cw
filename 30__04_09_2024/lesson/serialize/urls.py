from django.urls import path

from .views import *

urlpatterns = [
    path('post/', GetPostListView.as_view(), name='post_list'),
    path('category/', GetCategoryList.as_view(), name='category_list'),

]