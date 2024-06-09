from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=True)

    class Meta:
        verbose_name = 'Категория',
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, default='admin')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Пост',
        verbose_name_plural = 'Посты'
        ordering = ['id']

    def __str__(self):
        return self.title


class Comments(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50, null=False, blank=False)
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Комментарий',
        verbose_name_plural = 'Комментарии'
        ordering = ['id']

    def __str__(self):
        return self.author
