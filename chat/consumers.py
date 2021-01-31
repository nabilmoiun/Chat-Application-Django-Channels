import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Messages, Room


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def new_message(self, data):
        user = get_object_or_404(User, username=data['user'])
        room = get_object_or_404(Room, room_name=data['room_name'])
        message = data['message']
        newMessage = Messages.objects.create(
            author=user,
            message=message,
            room=room
        )
        author = newMessage.author.username
        return self.send_chat_message(message, author)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    commands = {
        'new-message': new_message
    }

    def receive(self, text_data):
        data = json.loads(text_data)
        action = data['command']
        self.commands[action](self, data)

    def send_chat_message(self, message, author):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author': author
            }
        )

    def send_message(self, messages):
        self.send(text_data=json.dumps(messages))

    def chat_message(self, event):
        message = event['message']
        author = event['author']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'author': author
        }))
