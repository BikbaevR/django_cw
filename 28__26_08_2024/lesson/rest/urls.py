from django.urls import path
from .views import *


urlpatterns = [
    path('test', GetPostListView.as_view(), name='test'),
    path('test/<int:pk>', GetPostDetailView.as_view(), name='test2'),
]