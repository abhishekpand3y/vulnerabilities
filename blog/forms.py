from blog.models import Post
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput

class UserCreat(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=PasswordInput)
    class Meta:
        model = User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','desc']
        labels={'title':'Title','desc':'Discription'}
    