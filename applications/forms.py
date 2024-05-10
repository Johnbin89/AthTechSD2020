from django.forms import ModelForm
from django import forms
from applications.models import ApplicationForm, ApplicationSubField,ApplicationYpanForm,ApplicationYpanSubField
from accounts.models import SubField
from itertools import chain

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
        self.fields['file'].widget = forms.TextInput(attrs={
            'name': 'file',
            })
        self.fields['file'].label = 'Αρχείο απόδειξης τεχνικής επάρκειας προσωπικού'

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


class UploadYpanDocumentForm(ModelForm):

    class Meta:
        model = ApplicationYpanForm
        fields = ['subfields', 'Civil_ExpDate' ] + ApplicationYpanForm.get_file_strs()
    
    #find the subfields that are not in pending esyd apps for this user
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user')
        super(UploadYpanDocumentForm, self).__init__(*args, **kwargs)
        esyd_subfields = ApplicationForm.objects.values_list('subfields', flat=True).filter(foreas = current_user.id,status='Εγκρίθηκε')
        used_subfields = ApplicationYpanForm.objects.values_list('subfields', flat=True).filter(foreas = current_user.id)
        notrejected_fields = used_subfields.exclude(status= 'Απορρίφθηκε')
        available_fields = SubField.objects.filter( pk__in=set(esyd_subfields))
        final_fields = available_fields.exclude( pk__in=set(notrejected_fields))
        self.fields['subfields'].queryset = final_fields
        for field_str in ApplicationYpanForm.get_file_strs():
            self.fields[field_str].widget = forms.TextInput(attrs={
                'name': field_str,
                })
            self.fields[field_str].label = ApplicationYpanForm.get_verbose_names().get(field_str)


class YpanStatusForm(ModelForm):
    class Meta:
        model = ApplicationYpanSubField
        fields = ['status', 'expDate']


    def __init__(self, *args, **kwargs):
        super(YpanStatusForm, self).__init__(*args, **kwargs)
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