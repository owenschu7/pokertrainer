from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')




