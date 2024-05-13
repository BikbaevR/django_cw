from django.contrib import admin
from .models import Post, Category


# Register your models here.


class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'published', 'rating', 'post_is_active']
    search_fields = ['title', 'published', 'rating']
    list_filter = ['published']


admin.site.register(Post, AdminPost)
admin.site.register(Category)
