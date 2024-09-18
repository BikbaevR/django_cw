from django.contrib import admin
from .models import *

admin.site.register([Category, Prodavec, Pokupatel, Producti, Order, Feedback])