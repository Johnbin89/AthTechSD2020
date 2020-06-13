from django.shortcuts import render, redirect
from django.contrib import messages
#from django.contrib.auth import authenticate, logout
#from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    context = {'home': True}
    # messages.success(request, 'Hello')
    return render(request, 'index.html', context)

def services(request):
    context = {'services_page': True}
    return render(request, 'services.html', context)

def contactus(request):
    context = {'contact_page': True}
    return render(request, 'contactus.html', context)