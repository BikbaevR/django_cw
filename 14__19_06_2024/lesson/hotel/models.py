from django.db import models
from django.contrib.auth.models import User


class HotelRoom(models.Model):
    number = models.IntegerField()
    type = models.ForeignKey('RoomType', on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    photo = models.ImageField(upload_to='hotel', default='hotel/default.jpg')

    def __str__(self):
        return str(self.number)


class RoomType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey('HotelRoom', on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.room
