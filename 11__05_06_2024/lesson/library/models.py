from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='books/%d-%m-%y')
    # file = models.FileField(upload_to='books/%d-%m-%y', null=True, blank=True, default=None)
    description = models.TextField(null=True)
    author = models.ManyToManyField('Author', null=True, blank=False, related_name='author')
    category = models.ForeignKey('Category', null=True, blank=False, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"



class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='authors/%d-%m-%y')
    bio = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories/%d-%m-%y')

    def __str__(self):
        return f"{self.name}"
