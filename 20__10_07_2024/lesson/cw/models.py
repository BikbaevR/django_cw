from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField()

    def __str__(self):
        return self.user_id


class Dish(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')
    price = models.FloatField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ShoppingCard(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username


class OrderElement(models.Model):
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish_id
