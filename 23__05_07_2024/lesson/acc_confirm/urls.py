from django.urls import path
from .views import *

urlpatterns = [
    path('reg', register, name='register'),
    path('log', signIn, name='signIn'),
]