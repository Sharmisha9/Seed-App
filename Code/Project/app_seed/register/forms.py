from email.policy import default
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


# https://stackoverflow.com/questions/31130706/dropdown-in-django-model
FILE_CONTENT = (
    ('soil', "SOIL"),
    ('zip', "ZIP"),
    ('season', "SEASON"),
    ('crop', "CROP"),
    ('temperature',"TEMPERATURE"),
    ('admin_file', "CSV")
)
class File(forms.Form):
        title = forms.CharField(label="Enter Title CVS", max_length= 200)
        file = forms.FileField()
        type = forms.CharField(label="Choose a file type", widget = forms.Select(choices=FILE_CONTENT))
    

