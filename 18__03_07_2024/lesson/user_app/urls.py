from django.urls import path
from .views import *


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]