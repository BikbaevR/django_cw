from django.urls import path, re_path
from .views import index, about, contact, publication

urlpatterns = [
    path('', index, name='index_page'),
    path('about', about, name='about_page'),
    path('contact', contact, name='contact_page'),
    re_path(r'^post', publication),
]