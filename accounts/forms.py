from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ApplicantProfile
from django.views.generic.edit import UpdateView


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
