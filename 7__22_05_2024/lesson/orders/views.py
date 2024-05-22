from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Order


# Create your views here.


def index(request):

    # product = Product.objects.all()

    # product = Product.objects.first()
    # product = Product.objects.last()
    # print(product)
    # order = Order.objects.earliest('created') #самую ранюю запись
    # order = Order.objects.earliest('-created')  # самую ранюю запись
    # order = Order.objects.latest('created')  # самую ранюю запись
    # order = Order.objects.filter(user='Пользователь').exists()  # самую ранюю запись

    # order = Order.objects.get(id=1)
    # print(order)
    # print(order.get_next_by_created())

    #lf <
    #lte <=
    #gt >
    #gte >=

    # order = Order.objects.exclude(user='Пользователь')
    # print(order)




    return render(request, 'orders/index.html')