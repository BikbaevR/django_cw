from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    SUBSCRIBE_TYPE = [
        ('scuf', 'Скуф'),
        ('shuxa', 'Шуха'),
        ('daddy', 'Daddy')
    ]
    subscribe_expired = models.DateField(null=True)
    subscribe_type = models.CharField(max_length=10, choices=SUBSCRIBE_TYPE)
    balance = models.PositiveBigIntegerField(default=0)
