from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)

    pub_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=100)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.author