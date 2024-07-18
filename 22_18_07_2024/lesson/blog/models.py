from django.db import models
from user_app.models import *



class Category(models.Model):
    name = models.CharField(max_length=100)
    is_hot = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='posts/category')


class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')


class PostMedia(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='post/media')


class Tag(models.Model):
    name = models.CharField(max_length=200)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
