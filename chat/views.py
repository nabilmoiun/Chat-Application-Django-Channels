import json

from django.contrib import messages
from django.views.generic import View
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from django.utils.safestring import mark_safe
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import SignupForm
from .models import Messages, Room
from django.contrib.auth.models import User
from .decorators import is_user_authenticated


@login_required
def index(request):
    return render(request, 'chat/index.html', {})


@login_required
def room(request, room_name):
    user = User.objects.get(pk=request.user.pk)
    room, created = Room.objects.get_or_create(room_name=room_name)
    if created:
        room_name = room.room_name
    messages = Messages.objects.filter(room__room_name=room_name)
    rooms = Room.objects.all()

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user': user,
        'username': request.user.username,
        'room_messages': messages,
        'rooms': rooms
    })


@is_user_authenticated
def signup_view(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect('login')
    return render(request, 'chat/signup.html', {"form": form})


@is_user_authenticated
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/chat/')
        else:
            messages.warning(request, "Unauthorized Credentials")
            return redirect('login')
    return render(request, 'chat/login.html', {})


def logout_view(request):
    logout(request)
    return redirect('login')