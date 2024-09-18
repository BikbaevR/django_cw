from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Prodavec(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Pokupatel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



class Producti(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    price = models.FloatField()
    prodavec = models.ForeignKey(Prodavec, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    pokupatel = models.ForeignKey(Pokupatel, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Producti)

    def __str__(self):
        return str(self.date)


class Feedback(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
