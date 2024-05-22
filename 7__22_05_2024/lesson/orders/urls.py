from django.urls import path
from .views import index, product_info


urlpatterns = [
    path('', index, name='index'),
    path('product_info/<slug:slug>', product_info, name='product-info')
]