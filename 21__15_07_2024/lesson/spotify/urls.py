from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryView.as_view(), name='category_view'),
    path('genre/<int:pk>', OneCategoryView.as_view(), name='genre_music'),
    path('music/<int:pk>', MusicDetail.as_view(), name='music_detail'),
    path('history/', HistoryView.as_view(), name='history')
]