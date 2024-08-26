from django.db import models


class MainUser(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    token = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

