from django.shortcuts import render, redirect
from user.models import User

# Create your views here.

def index(request):
    return render(request, 'layout/index.html')

def view_about(request):
    return render(request, 'layout/about.html')
