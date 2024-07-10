from django.contrib import admin
from .models import *


admin.site.register([Category, Order, Dish, ShoppingCard, OrderElement])
