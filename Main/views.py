from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    return render(request, 'Main/web.html')

def login(request):
    return render(request, 'Main/login.html')

def signup(request):
    return render(request, 'Main/signup.html')

def learn(request):
    return render(request, 'Main/learn.html')

def home(request):
    return render(request , 'Main/home.html')

def about(request):
    return render(request, 'Main/about.html')

def uploadvid(request):
    return render(request, 'Main/uploadvid.html')

def uploadaud(request):
    return render(request,'Main/uploadaud.html')

def uploadimg(request):
    return render(request,'Main/uploadimg.html')

