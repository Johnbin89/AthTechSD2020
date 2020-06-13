from django.core.management.base import BaseCommand, CommandError
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail  
from applications.models import ApplicationYpanForm
from background_task import background

@background(schedule=1)
def run_reminder():
    print('start')
    for ypanApp in ApplicationYpanForm.objects.filter(ypan_subfields__status ='Εγκρίθηκε'):

        dateToSearch = date.today() + relativedelta(months=1)

        for subField in ypanApp.ypan_subfields.filter(expDate = dateToSearch):

            userEmail = subField.application.foreas.email
            subField = subField.subField.regulation.regulation + ' - ' + subField.subField.subField

            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας για το ' + subField + ' λήγει σε 1 μήνα.',
                    'ypan.info@gmail.com',
                    [userEmail])

    for ypanApp in ApplicationYpanForm.objects.filter(ypan_subfields__status ='Εγκρίθηκε'):

        dateToSearch = date.today() + relativedelta(months=3)

        for subField in ypanApp.ypan_subfields.filter(expDate = dateToSearch):

            userEmail = subField.application.foreas.email
            subField = subField.subField.regulation.regulation + ' - ' + subField.subField.subField

            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας για το ' + subField + ' λήγει σε 3 μήνες.',
                    'ypan.info@gmail.com',
                    [userEmail])
