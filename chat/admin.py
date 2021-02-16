from django.contrib import admin
from .models import Messages, Room, UserToUserConnection, UserMessages

class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model = Messages
    list_display = ['__str__', 'author', 'room']


admin.site.register(Messages, MessageAdmin)
admin.site.register(Room)
admin.site.register(UserToUserConnection)
admin.site.register(UserMessages)