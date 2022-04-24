from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# I think this method would not be useful if I am be a backend developer.

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")