from django.forms import ModelForm
from django import forms
from applications.models import ApplicationForm, ApplicationSubField,ApplicationYpanForm,ApplicationYpanSubField
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


class UploadYpanDocumentForm(ModelForm):

    class Meta:
        model = ApplicationYpanForm
        fields = ['subfields', 'Non_Bankruptcy_Cert_1','Non_Bankruptcy_Cert_2','Non_Clearance_Cert','Non_Force_Arrange_Cert'
        ,'GEMI_Cert','Tax_Clear_Cert','Insurance_Liability_Cert','Civil_ID','Civil_ExpDate','Balance_Sheet_3Y','Art_Of_Incorporation'
            ,'GEMI_NoMod_Cert','Foreign_Activity_Decl','Coord_Group_Decl']
    
    #find the subfields that are not in pending esyd apps for this user
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user')
        super(UploadYpanDocumentForm, self).__init__(*args, **kwargs)
        esyd_subfields = ApplicationForm.objects.values_list('subfields', flat=True).filter(foreas = current_user.id)
        accepted_subfields = SubField.objects.filter(children__status = 'Εγκρίθηκε', pk__in=set(esyd_subfields))
        used_subfields = ApplicationYpanForm.objects.values_list('subfields', flat=True).filter(foreas = current_user.id)
        _subfields = accepted_subfields.exclude(pk__in = set(used_subfields))
        self.fields['subfields'].queryset = _subfields

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