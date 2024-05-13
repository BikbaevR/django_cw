from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, db_index=True, unique_for_date='published') # униакальная по этому полю на день
    description = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)