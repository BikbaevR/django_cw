from django.db import models
from user_app.models import Account


# Create your models here.
class Chat(models.Model):
    is_group = models.BooleanField(default=False)
    owner_id = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, related_name='chats')
    is_premium = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='chats/logo', null=True, blank=True)
    participants = models.ManyToManyField(Account, through='Participant', blank=True)


class Participant(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    participant = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='chat/messages', null=True, blank=True)
