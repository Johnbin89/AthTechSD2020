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


class ProfileForm(forms.ModelForm):

    class Meta:
        model = ApplicantProfile
        fields = ['companyName', 'distTitle', 'afm', 'doy', 'gemi', 'address', 'postalCode', 'phone', 'fax', 'email',
              'contactPerson']


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['afm'] = forms.CharField(label='ΑΦΜ' ,widget=forms.TextInput(attrs={'maxlength': 9,
        'minlength': 9,
        'onkeypress': "return (event.charCode == 8 || event.charCode == 0 || event.charCode == 13) ? null : event.charCode >= 48 && event.charCode <= 57",
        }))
        self.fields['postalCode'] = forms.CharField(label='Ταχ. Κώδικας' ,widget=forms.TextInput(attrs={'maxlength': 5,
        'minlength': 5,
        'onkeypress': "return (event.charCode == 8 || event.charCode == 0 || event.charCode == 13) ? null : event.charCode >= 48 && event.charCode <= 57",
        }))
        self.fields['phone'] = forms.CharField(label='Τηλέφωνο' ,widget=forms.TextInput(attrs={'maxlength': 10,
        'minlength': 10,
        'onkeypress': "return (event.charCode == 8 || event.charCode == 0 || event.charCode == 13) ? null : event.charCode >= 48 && event.charCode <= 57",
        }))

        self.fields['email'] = forms.EmailField()
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'