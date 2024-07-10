from django.shortcuts import render, redirect

from django.views.generic import ListView, DeleteView
from django.views import View
from .models import *


class MainPage(ListView):
    model = Dish
    template_name = 'cw/index.html'
    context_object_name = 'dishes'


class ShoppingCardView(ListView):
    model = ShoppingCard
    template_name = 'cw/shoppingCard.html'
    context_object_name = 'shoppingCards'

    def get_queryset(self):
        return ShoppingCard.objects.filter(user_id=self.request.user)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
        # context['final_price'] =



def clear_ShoppingCard(request):
    data = ShoppingCard.objects.filter(user_id=request.user)
    data.delete()
    return redirect('index')

#Сейчас одинаковы заказы дублируются, поздно вспомнил об этом
class AddToShopingCard(View):
    def post(self, request):
        id = request.POST['id']
        quantity = request.POST['quantity']

        newRec = ShoppingCard()
        newRec.dish_id = Dish.objects.get(pk=id)
        newRec.user_id = request.user
        newRec.quantity = quantity
        newRec.save()
        return redirect('index')

def Checkout(request):
    datas = ShoppingCard.objects.filter(user_id=request.user)
    for data in datas:
        order = OrderElement()
        order.dish_id = data.dish_id.id
        order.quantity = data.quantity

    return redirect('index')

