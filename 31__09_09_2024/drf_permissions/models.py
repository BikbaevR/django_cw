from django.db import models
from django.contrib.auth.models import AbstractUser


#pip install djangorestframework-simplejwt



class User(AbstractUser):
    items = models.ManyToManyField('Item')



class Game(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/games/')


class Item(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icons/items/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    options = models.ManyToManyField('Option')



class Type(models.Model):
    label = models.CharField(max_length=255)
    TYPES = [
        ('select', 'Select'),
        ('checkbox', 'Checkbox'),
    ]
    type = models.CharField(choices=TYPES, max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Option(models.Model):
    label = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    sold_at = models.DateField(null=True, blank=True)


class PaymentHistory(models.Model):

    TYPE_CHOICES = [
        ('add', 'пополнение'),
        ('buy', 'купил'),
        ('sold', 'продал')
    ]

    value = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)