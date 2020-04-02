from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth import authenticate, logout
#from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    context = {'home': True}
    messages.success(request, 'Hello')
    return render(request, 'index.html', context)
