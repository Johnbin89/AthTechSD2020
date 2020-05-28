import uuid
import datetime

from django.db import models
from accounts.models import ApplicantProfile, SubField

# Create your models here.
from django.urls import reverse

#application foreas -> esyd
class ApplicationForm(models.Model):
    foreas = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    subfields = models.ManyToManyField(SubField, verbose_name='Πεδια', through='ApplicationSubField')
    status_esyd_choices = [
        ('Σε εκκρεμότητα', 'Σε εκκρεμότητα'),
        ('Απορρίφθηκε', 'Απορρίφθηκε'),
        ('Εγκρίθηκε', 'Εγκρίθηκε')
    ]
    status = models.CharField(max_length=30, verbose_name='Κατασταση', choices=status_esyd_choices, default='Σε εκκρεμότητα')
    date = models.DateField(default=datetime.date.today, verbose_name='Ημ/νία υποβολής')
    file = models.FileField(upload_to='applications/static/esyd_files', verbose_name="Αρχείο απόδειξης τεχνικής επάρκειας προσωπικού")

    def get_absolute_url(self):
        return reverse('Application', args=[self.pk])


#subfields of an application to esyd
class ApplicationSubField(models.Model):
    subField = models.ForeignKey(SubField, default=1, on_delete=models.CASCADE, related_name='children')
    application = models.ForeignKey(ApplicationForm, default=1, on_delete=models.CASCADE, related_name='children')
    status_esyd_sub_choices = [
        ('Σε εκκρεμότητα', 'Σε εκκρεμότητα'),
        ('Απορρίφθηκε', 'Απορρίφθηκε'),
        ('Εγκρίθηκε', 'Εγκρίθηκε')
    ]
    status = models.CharField(max_length=30, verbose_name="Κατάσταση", choices=status_esyd_sub_choices, default='Σε εκκρεμότητα')
    expDate = models.DateField(verbose_name="Ημερομηνία λήξης", null=True)

    class Meta:
        verbose_name = "Πεδίο"
        verbose_name_plural = "Πεδία"
        ordering = ['subField']

    def __str__(self):
        return self.subField.regulation.regulation + ' - ' + self.subField.subField


