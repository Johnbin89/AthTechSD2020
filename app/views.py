from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from app.forms import SignUpForm


def index(request):
    context = {'home': True}
    messages.success(request, 'Hello')
    return render(request, 'index.html', context)


def login(request):
    context = {'login': True}
    return render(request, 'registration/login.html', context)


# def register(request):
#     return render(request, 'registration/register.html', {})


def register(request):
    context = {'register': True}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was created successfully!')
            return redirect('login')
        else:
            for err in form.errors.values():
                messages.error(request, err)
    else:
        form = SignUpForm()
    context['form'] = form
    return render(request, 'registration/register.html', context)

