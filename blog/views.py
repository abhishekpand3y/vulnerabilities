from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post
from .forms import UserCreat, PostForm

# Create your views here.

#Homepage
def index(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})

#about me
def aboutme(request):
    return render(request,'blog/about.html')

#contact
def contact(request):
    return render(request,'blog/contact.html')

#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        return render(request,'blog/dashboard.html',{'posts':posts})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data["username"]
                upass=fm.cleaned_data["password"]
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=AuthenticationForm()
        return render(request,'blog/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#signup
def signup(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=UserCreat(request.POST)
            if fm.is_valid():
                messages.success(request,'Congratulations ! You have become an Author')
                fm.save()
        else:        
            fm = UserCreat()
        return render(request,'blog/signup.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

#Add a POST
def addpost(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=PostForm(request.POST)
            if fm.is_valid():
                #messages.success("Post Created Successfully")
                fm.save()
                fm=PostForm()
        else:
            fm=PostForm()
        return render(request,'blog/post.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

#Update a POST
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            postid=Post.objects.get(pk=id)
            fm=PostForm(request.POST,instance=postid)
            if fm.is_valid():
                #messages.success("Post Created Successfully")
                fm.save()                
        else:
            postid=Post.objects.get(pk=id)
            fm=PostForm(instance=postid)
        return render(request,'blog/post.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


#Delete a POST
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=="POST":
            postid=Post.objects.get(pk=id)
            postid.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
