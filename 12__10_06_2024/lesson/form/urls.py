from django.urls import path

from .views import *

urlpatterns = [
    path('form', index, name='index'),
    path('student', student, name='student'),
]