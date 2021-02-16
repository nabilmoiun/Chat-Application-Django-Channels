from django.urls import re_path, path

from .consumers import ChatConsumer, ChatConsumerUserToUser

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
    # re_path(r'ws/chat/user/(?P<connection_id>\w+)/$', ChatConsumerUserToUser.as_asgi()),
    path('ws/chat/user/<str:connection_id>/', ChatConsumerUserToUser.as_asgi()),
]
