from django.db import models
from user_app.models import *


class Transaction(models.Model):
    ORDER_TYPE = [
        ('basic', 'Basic'),
        ('family', 'Family'),
        ('premium', 'Premium'),
    ]
    STATUS = [
        ('created', 'Created'),
        ('processing', 'Processing'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled')
    ]

    order_type = models.CharField(max_length=200, choices=ORDER_TYPE)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)
    amount = models.PositiveBigIntegerField()
