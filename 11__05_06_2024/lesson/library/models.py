from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='books/%d-%m-%y')
    file = models.FileField(upload_to='books/%d-%m-%y', null=True, blank=True, default=None)
