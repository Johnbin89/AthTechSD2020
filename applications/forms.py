
# class ApplicationForm():
from django.forms import ModelForm

from applications.models import ApplicationForm


class UploadDocumentForm(ModelForm):

    class Meta:
        model = ApplicationForm
        fields = ['subfields', 'file']


