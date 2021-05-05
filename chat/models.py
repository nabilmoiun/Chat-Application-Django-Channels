import uuid
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_name = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name


class Messages(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.message[:20]


class UserToUserConnection(models.Model):
    connection_id = models.CharField(max_length=500)
    users = models.ManyToManyField(User)
    messages = models.ManyToManyField('UserMessages')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.connection_id


class UserMessages(models.Model):
    message = models.TextField(null=True, blank=True)
    connection = models.ForeignKey(UserToUserConnection, related_name='userMessages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='userMessages', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message