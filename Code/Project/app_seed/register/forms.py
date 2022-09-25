from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# from django.db import models


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    phone = forms.CharField(label="Enter phone #")
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    #
    class Meta:
        model = User
        fields = ["username", "email", "phone", "password1", "password2"]