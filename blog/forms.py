from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User

class User_Creation(UserCreationForm):
    class Meta:
        model = User 

    