from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    return render(request, 'Main/index.html')

def login(request):
    return render(request, 'Main/login.html')

def signup(request):
    return render(request, 'Main/signup.html')