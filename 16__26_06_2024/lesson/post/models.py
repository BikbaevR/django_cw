from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%d-%m-%Y')


