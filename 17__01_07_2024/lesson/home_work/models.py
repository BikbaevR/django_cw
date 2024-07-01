from django.db import models


class Screenshot(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='screenshots/')


class Video(models.Model):
    name = models.CharField(max_length=100, null=True)
    video = models.FileField(upload_to='videos/')
    category = models.ForeignKey('VideoCategory', on_delete=models.CASCADE)


class VideoCategory(models.Model):
    name = models.CharField(max_length=100)


class Audio(models.Model):
    name = models.CharField(max_length=100, null=True)
    audio = models.FileField(upload_to='audios/')
    category = models.ForeignKey('AudioCategory', on_delete=models.CASCADE)


class AudioCategory(models.Model):
    name = models.CharField(max_length=100)
