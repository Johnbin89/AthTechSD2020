from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import foreas_required
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignUpForm
from .models import ApplicantProfile,Regulation,SubField
from django.views.generic.edit import UpdateView, CreateView


# Create your views here.
@login_required
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



@method_decorator([login_required, foreas_required], name='dispatch')
class ForeasProfile(UpdateView):
    slug_field = 'user'
    slug_url_kwarg = 'user_id'
    model = ApplicantProfile
    template_name = 'profile.html'
    fields = ['companyName', 'distTitle', 'afm','doy','gemi','address','postalCode','phone','fax','email','contactPerson']


class NewRegulation(CreateView):
    model = Regulation
    template_name = 'new_regulation.html'
    fields = '__all__'

class NewSubField(CreateView):
    model = SubField
    template_name = 'new_subfield.html'
    fields = '__all__'