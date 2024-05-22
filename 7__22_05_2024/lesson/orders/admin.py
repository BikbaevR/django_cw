from django.contrib import admin
from .models import Category, Product, Order


# Register your models here.

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

    prepopulated_fields = {'slug': ('name',)}


class AdminProduct(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

    prepopulated_fields = {'slug': ('name',)}


class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'created']
    search_fields = ['user']
    list_filter = ['user', 'created']


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Order, AdminOrder)
