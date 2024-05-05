import uuid
import datetime

from django.db import models
from accounts.models import ApplicantProfile, SubField

# Create your models here.
from django.urls import reverse
from django_drf_filepond.models import StoredUpload

def generate_filename(self, filename):
    url = "esyd_applications/%s/%s" % (self.foreas.foreas_profile.companyName, filename)
    return url

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
    file = models.ForeignKey(StoredUpload, on_delete=models.CASCADE)

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


def generate_filename_ypan(self, filename):
    url = "ypan_applications/%s/%s" % (self.foreas.foreas_profile.companyName, filename)
    return url


#application foreas -> ypan
class ApplicationYpanForm(models.Model):
    foreas = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    subfields = models.ManyToManyField(SubField, verbose_name='Πεδια', through='ApplicationYpanSubField')
    status_ypan_choices = [
        ('Σε εκκρεμότητα', 'Σε εκκρεμότητα'),
        ('Απορρίφθηκε', 'Απορρίφθηκε'),
        ('Εγκρίθηκε', 'Εγκρίθηκε')
    ]
    status = models.CharField(max_length=30, verbose_name='Κατασταση', choices=status_ypan_choices, default='Σε εκκρεμότητα')
    date = models.DateField(default=datetime.date.today, verbose_name='Ημ/νία υποβολής')
    Non_Bankruptcy_Cert_1= models.FileField(upload_to=generate_filename_ypan, verbose_name="Πιστοποιητικό Πρωτοδικείου περί μη πτώχευσης σε ισχύ")
    Non_Bankruptcy_Cert_2= models.FileField(upload_to=generate_filename_ypan, verbose_name="Πιστοποιητικό Πρωτοδικείου περί μη κατάθεσης αίτησης πτωχεύσεως σε ισχύ")
    Non_Clearance_Cert= models.FileField(upload_to=generate_filename_ypan, verbose_name="Πιστοποιητικό Πρωτοδικείου περί μη θέσης σε εκκαθάριση σε ισχύ")
    Non_Force_Arrange_Cert= models.FileField(upload_to=generate_filename_ypan, verbose_name="Πιστοποιητικό Πρωτοδικείου περί μη θέσης σε αναγκαστική διαχείριση σε ισχύ")
    GEMI_Cert= models.FileField(upload_to=generate_filename_ypan, verbose_name="Πιστοποιητικό ΓΕΜΗ Γενικής Χρήσης και Εκπροσώπησης")
    Tax_Clear_Cert = models.FileField(upload_to=generate_filename_ypan, verbose_name="Αποδεικτικό ενημερότητας για χρέη προς το Δημόσιο")
    Insurance_Liability_Cert= models.FileField(upload_to=generate_filename_ypan, verbose_name="Βεβαίωση ΙΚΑ περί ασφαλιστικής ενημερότητας σε ισχύ")
    Civil_ID= models.FileField(upload_to=generate_filename_ypan, verbose_name="Βεβαίωση ασφάλισης επαγγελματικής αστικής ευθύνης για την κάλυψη κινδύνων των παρεχόμενων υπηρεσιών")
    Civil_ExpDate = models.DateField(verbose_name='Ημ/νία λήξης ασφάλισης')
    Balance_Sheet_3Y = models.FileField(upload_to=generate_filename_ypan, verbose_name="Ισολογισμοί τριών τελευταίων ετών")
    Art_Of_Incorporation= models.FileField(upload_to=generate_filename_ypan, verbose_name="Κωδικοποιημένο καταστατικό της εταιρείας")
    GEMI_NoMod_Cert= models.FileField(upload_to=generate_filename_ypan, verbose_name="Βεβαίωση περί μη τροποποίησης του πιστοποιητικού ΓΕΜΗ")
    Foreign_Activity_Decl= models.FileField(upload_to=generate_filename_ypan, verbose_name="Υπεύθυνη δήλωση του κοινοποιημένου οργανισμού για τη δραστηριοποίησή του ή μη σε άλλες χώρες")
    Coord_Group_Decl= models.FileField(upload_to=generate_filename_ypan, verbose_name="Υπεύθυνη δήλωση του κοινοποιημένου φορέα για τη συμμετοχή του ή μη στις ομάδες συντονισμού")
    def get_absolute_url(self):
        return reverse('ypan_application', args=[self.pk])

#subfields of an application to ypan
class ApplicationYpanSubField(models.Model):
    subField = models.ForeignKey(SubField, default=1, on_delete=models.CASCADE, related_name='ypan_apps')
    application = models.ForeignKey(ApplicationYpanForm, default=1, on_delete=models.CASCADE, related_name='ypan_subfields')
    status_ypan_sub_choices = [
        ('Σε εκκρεμότητα', 'Σε εκκρεμότητα'),
        ('Απορρίφθηκε', 'Απορρίφθηκε'),
        ('Εγκρίθηκε', 'Εγκρίθηκε')
    ]
    status = models.CharField(max_length=30, verbose_name="Κατάσταση", choices=status_ypan_sub_choices, default='Σε εκκρεμότητα')
    expDate = models.DateField(verbose_name="Ημερομηνία λήξης", null=True)

    class Meta:
        verbose_name = "Πεδίο"
        verbose_name_plural = "Πεδία"
        ordering = ['subField']

    def __str__(self):
        return self.subField.regulation.regulation + ' - ' + self.subField.subField
