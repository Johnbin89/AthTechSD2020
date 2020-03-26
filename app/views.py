from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from app.forms import SignUpForm


def index(request):
    context = {'home': True}
    messages.success(request, 'Hello')
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'registration/login.html', {})


# def register(request):
#     return render(request, 'registration/register.html', {})


def register(request):
    # if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base')
        else:
            form = SignUpForm()
        return render(request, 'registration/register.html', {'form': form})

