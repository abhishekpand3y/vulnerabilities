from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

#Homepage
def index(request):
    return render(request,'blog/home.html')

#about me
def aboutme(request):
    return render(request,'blog/about.html')

#contact
def contact(request):
    return render(request,'blog/contact.html')

#dashboard
def dashboard(request):
    return render(request,'blog/dashboard.html')

#login
def user_login(request):
    return render(request,'blog/login.html')

#logout
def user_logout(request):
    return render(request,'blog/logout.html')

#singup
def signup(request):
    form = UserCreationForm()
    return render(request,'blog/signup.html',{'form':form})