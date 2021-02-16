from django.urls import path
from .views import index, room, connection

urlpatterns = [
    path('user/<str:connection_id>/', connection, name='user_connection'),
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]