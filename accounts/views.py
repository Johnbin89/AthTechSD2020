from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm,ProfileForm,NewRegulation,NewSubField
from .models import ApplicantProfile,Regulation
from django.views.generic.edit import UpdateView


# Create your views here.
def logout_view(request):
    logout(request)
    messages.info(request, 'You have logged out successfully.')
    return redirect('index')


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


def regulation_view(request):
    return render(request,'regulation_list.html', {'regulations': Regulation.objects.all()})