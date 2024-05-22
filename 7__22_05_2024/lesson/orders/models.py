from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'
        ordering = ['id']


class Order(models.Model):
    user = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = 'Заказы'
        ordering = ['id']
