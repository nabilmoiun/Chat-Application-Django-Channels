from django.contrib.auth.models import User


def generate_connection_id(connected_by, connecting_to):
    connection_id = None
    sender = User.objects.get(username=connected_by)
    receiver = User.objects.get(username=connecting_to)
    if sender.id > receiver.id:
        connection_id = f"{sender}.{receiver}"
    else:
        connection_id = f"{receiver}.{sender}"
    return connection_id
