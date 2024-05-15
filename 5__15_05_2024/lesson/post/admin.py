from django.contrib import admin

from .models import Category, Post


# Register your models here.

class CategoryPost(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class PostPost(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    search_fields = ['title']
    list_filter = ['title', 'published_at', 'category']


admin.site.register(Category, CategoryPost)
admin.site.register(Post, PostPost)
