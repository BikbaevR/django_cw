from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    published_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['id']

    def __str__(self):
        return self.title