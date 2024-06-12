from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_form, name='login_form'),
    path('profile/', profile, name='profile'),
    path('logout/', loqout_view, name='loqout_page'),

]