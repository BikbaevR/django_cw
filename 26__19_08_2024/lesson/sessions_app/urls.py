from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
]