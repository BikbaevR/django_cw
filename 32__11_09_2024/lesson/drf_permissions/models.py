from django.db import models
from django.contrib.auth.models import AbstractUser


#pip install djangorestframework-simplejwt



class User(AbstractUser):
    items = models.ManyToManyField('Item')

    def __str__(self):
        return self.username


    def balance(self):

        sum = 0

        for history in self.histories.all():
            if history.type == 'add' or history.type == "sold":
                sum += history.value
            else:
                sum -= history.value
        return sum


class Game(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/games/')

    def __str__(self):
        return self.name


class Item(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='icons/items/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    options = models.ManyToManyField('Option')

    def __str__(self):
        return self.name



class Type(models.Model):
    label = models.CharField(max_length=255)
    TYPES = [
        ('select', 'Select'),
        ('checkbox', 'Checkbox'),
    ]
    type = models.CharField(choices=TYPES, max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='types')

    def __str__(self):
        return f"{self.game.name} - {self.label}"

class Option(models.Model):
    label = models.CharField(max_length=255)
    color = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.label

class Lot(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    sold_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.price)


class PaymentHistory(models.Model):

    TYPE_CHOICES = [
        ('add', 'пополнение'),
        ('buy', 'купил'),
        ('sold', 'продал')
    ]

    value = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='histories')
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return self.type