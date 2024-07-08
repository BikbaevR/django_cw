from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('class/', IndexView.as_view(), name='index_class'),
    path('template_view/', IndexView2.as_view(), name='index_class_2'),

]