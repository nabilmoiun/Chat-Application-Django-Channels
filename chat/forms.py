from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"class": "form-control", "placeholder": "Enter username"})
        self.fields['password1'].widget.attrs.update({"class": "form-control", "placeholder": "Enter password"})
        self.fields['password2'].widget.attrs.update({"class": "form-control", "placeholder": "Confirm password"})
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean(self):
        username = self.cleaned_data['username']
        if User.objects.filter(Q(username__icontains=username)).exists():
            raise ValidationError("Username already exists")
        return self.cleaned_data