from django.urls import path
from .views import *

urlpatterns = [
    path('add_to_sc/', AddToShopingCard.as_view(), name='add_to_sc'),

    path('', MainPage.as_view(), name='index'),
    path('shoping_card/', ShoppingCardView.as_view(), name='shoping_card'),
    path('clear/', clear_ShoppingCard, name='clear_shopping_card'),
    path('checkout/', Checkout, name='heckout')
]