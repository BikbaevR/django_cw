from django.contrib import admin
from .models import Category, Post, Comments


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'author', 'category']
    search_fields = ['title', 'category']
    list_filter = ['title', 'category']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['author']
    search_fields = ['author']
    list_filter = ['author']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
