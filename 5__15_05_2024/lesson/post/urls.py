from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path('', index, name='index_page'),
    path('about', about, name='about_page'),
    path('contact', contact, name='contact_page')
]