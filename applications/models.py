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
    file = models.OneToOneField(StoredUpload, on_delete=models.CASCADE)

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
    Non_Bankruptcy_Cert_1= models.OneToOneField(StoredUpload, related_name="non_bank_app_1", on_delete=models.CASCADE)
    Non_Bankruptcy_Cert_2= models.OneToOneField(StoredUpload, related_name="non_bank_app_2", on_delete=models.CASCADE)
    Non_Clearance_Cert= models.OneToOneField(StoredUpload, related_name="non_clear_app", on_delete=models.CASCADE)
    Non_Force_Arrange_Cert= models.OneToOneField(StoredUpload, related_name="non_forge_app", on_delete=models.CASCADE)
    GEMI_Cert= models.OneToOneField(StoredUpload, related_name="gemi_cert_app", on_delete=models.CASCADE)
    Tax_Clear_Cert = models.OneToOneField(StoredUpload, related_name="tax_clear_app", on_delete=models.CASCADE)
    Insurance_Liability_Cert= models.OneToOneField(StoredUpload, related_name="ins_lia_app", on_delete=models.CASCADE)
    Civil_ID= models.OneToOneField(StoredUpload, related_name="civil_id_app", on_delete=models.CASCADE)
    Civil_ExpDate = models.DateField(verbose_name='Ημ/νία λήξης ασφάλισης')
    Balance_Sheet_3Y = models.OneToOneField(StoredUpload, related_name="bal_sheet_app", on_delete=models.CASCADE)
    Art_Of_Incorporation= models.OneToOneField(StoredUpload, related_name="art_ink_app", on_delete=models.CASCADE)
    GEMI_NoMod_Cert= models.OneToOneField(StoredUpload, related_name="gemi_nomod_app", on_delete=models.CASCADE)
    Foreign_Activity_Decl= models.OneToOneField(StoredUpload, related_name="for_act_app", on_delete=models.CASCADE)
    Coord_Group_Decl= models.OneToOneField(StoredUpload, related_name="cord_group_app", on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('ypan_application', args=[self.pk])
    
    @classmethod
    def get_file_strs(cls)-> list[str]:
        return ['Civil_ID',
                'Non_Bankruptcy_Cert_1',
                'Non_Bankruptcy_Cert_2',
                'Non_Force_Arrange_Cert',
                'Non_Clearance_Cert',
                'GEMI_Cert',
                'Tax_Clear_Cert',
                'Insurance_Liability_Cert',
                'Balance_Sheet_3Y',
                'Art_Of_Incorporation',
                'GEMI_NoMod_Cert',
                'Foreign_Activity_Decl',
                'Coord_Group_Decl'
                ]

    @classmethod
    def get_verbose_names(cls)-> dict:
        return {
           'Non_Bankruptcy_Cert_1': "Πιστοποιητικό Πρωτοδικείου περί μη πτώχευσης σε ισχύ",
           'Non_Bankruptcy_Cert_2': "Πιστοποιητικό Πρωτοδικείου περί μη κατάθεσης αίτησης πτωχεύσεως σε ισχύ",
           'Non_Clearance_Cert': "Πιστοποιητικό Πρωτοδικείου περί μη θέσης σε εκκαθάριση σε ισχύ",
           'Non_Force_Arrange_Cert': "Πιστοποιητικό Πρωτοδικείου περί μη θέσης σε αναγκαστική διαχείριση σε ισχύ",
           'GEMI_Cert': "Πιστοποιητικό ΓΕΜΗ Γενικής Χρήσης και Εκπροσώπησης",
           'Tax_Clear_Cert': "Αποδεικτικό ενημερότητας για χρέη προς το Δημόσιο",
           'Insurance_Liability_Cert': "Βεβαίωση ΙΚΑ περί ασφαλιστικής ενημερότητας σε ισχύ",
           'Civil_ID': "Βεβαίωση ασφάλισης επαγγελματικής αστικής ευθύνης για την κάλυψη κινδύνων των παρεχόμενων υπηρεσιών",
           'Balance_Sheet_3Y': "Ισολογισμοί τριών τελευταίων ετών",
           'Art_Of_Incorporation': "Κωδικοποιημένο καταστατικό της εταιρείας",
           'GEMI_NoMod_Cert': "Βεβαίωση περί μη τροποποίησης του πιστοποιητικού ΓΕΜΗ",
           'Foreign_Activity_Decl': "Υπεύθυνη δήλωση του κοινοποιημένου οργανισμού για τη δραστηριοποίησή του ή μη σε άλλες χώρες",
           'Coord_Group_Decl': "Υπεύθυνη δήλωση του κοινοποιημένου φορέα για τη συμμετοχή του ή μη στις ομάδες συντονισμού",
        }

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
