from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ApplicantProfile,Regulation,SubField
from django.views.generic.edit import UpdateView,CreateView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy

from django.forms.models import inlineformset_factory


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            newProfile = ApplicantProfile(userName= user, email = user.email)
            newProfile.save()
        return user




class ProfileForm(UpdateView):
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


