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


    def __init__(self, *args, **kwargs):
        super(EsydStatusForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance', None)
        date_id_text = "expDate-form%s%s" % (instance.application.id, str(instance).replace(" ",""))
        status_id_text = "status-form%s%s" % (instance.application.id, str(instance).replace(" ",""))
        self.fields['expDate'].widget = forms.DateInput(format=('%Y-%m-%d'), attrs={
            'id': date_id_text,
            'placeholder': 'Επιλογή Ημ. Λήξης',
            'disabled':True})
        self.fields['status'].widget.attrs\
            .update({
                'id': status_id_text,
                'disabled':True
            })
