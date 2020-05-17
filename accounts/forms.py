from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User, ApplicantProfile, Regulation, SubField
from django.db import transaction
from django.urls import reverse_lazy

from django.forms.models import inlineformset_factory


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_foreas')
        widgets = {'is_foreas': forms.HiddenInput()}

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_foreas = True
        if commit:
            user.save()
            newProfile = ApplicantProfile(user=user, email=user.email)
            newProfile.save()
        return user
