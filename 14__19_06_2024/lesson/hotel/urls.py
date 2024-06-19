from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_room_type', create_room_type, name='create_room_type'),
    path('create_room', create_room, name='create_room'),
    path('create_reservation', create_reservation, name='create_reservation'),
]