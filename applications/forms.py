from django.forms import ModelForm
from django import forms
from applications.models import ApplicationForm, ApplicationSubField
from accounts.models import SubField


class UploadDocumentForm(ModelForm):

    class Meta:
        model = ApplicationForm
        fields = ['subfields', 'file']
    
    #find the subfields that are not in pending esyd apps for this user
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user')
        super(UploadDocumentForm, self).__init__(*args, **kwargs)
        used_subfields = ApplicationForm.objects.values_list('subfields', flat=True).filter(foreas = current_user.id)
        unused_subfields = SubField.objects.exclude(pk__in=set(used_subfields))
        self.fields['subfields'].queryset = unused_subfields

class EsydStatusForm(ModelForm):
    class Meta:
        model = ApplicationSubField
        fields = ['status', 'expDate']
        widgets = {
        'expDate': forms.DateInput(format=('%m/%d/%Y'), attrs={'placeholder':'Επιλογή Ημ. Λήξης', 'type':'date'}),
        }