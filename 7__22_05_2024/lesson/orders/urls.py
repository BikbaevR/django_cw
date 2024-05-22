from django.urls import path
from .views import index, product_info


urlpatterns = [
    path('', index, name='index'),
    path('product_info', product_info, name='product_info')
]