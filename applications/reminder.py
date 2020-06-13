from django.core.management.base import BaseCommand, CommandError
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail  
from applications.models import ApplicationYpanForm,ApplicationForm
from background_task import background

@background(schedule=1)
def run_reminder():
    print('start')

    oneMonthDate = date.today() + relativedelta(months=1)
    threeMonthDate = date.today() + relativedelta(months=2)

    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in ypanApp.ypan_subfields.filter(expDate = oneMonthDate):

            userEmail = subField.application.foreas.email
            subField =  subField.subField.subField
            regulation = subField.subField.regulation.regulation
            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το Υπουργείο Ανάπτυξης για το θεματικό πεδίο "' + subField + '" της νομοθεσίας "'+ regulation +'" λήγει σε 1 μήνα.',
                    'ypan.info@gmail.com',
                    [userEmail])

    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in ypanApp.ypan_subfields.filter(expDate = threeMonthDate):

            userEmail = subField.application.foreas.email
            subField =  subField.subField.subField
            regulation = subField.subField.regulation.regulation

            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το Υπουργείο Ανάπτυξης για το θεματικό πεδίο "' + subField + '" της νομοθεσίας "'+ regulation +'" λήγει σε 3 μήνες.',
                    'ypan.info@gmail.com',
                    [userEmail])


    for esydApp in ApplicationForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in esydApp.children.filter(expDate = oneMonthDate):

            userEmail = subField.application.foreas.email
            subField =  subField.subField.subField
            regulation = subField.subField.regulation.regulation
            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το ΕΣΥΔ για το θεματικό πεδίο "' + subField + '" της νομοθεσίας "'+ regulation +'" λήγει σε 1 μήνα.',
                    'ypan.info@gmail.com',
                    [userEmail])

    for esydApp in ApplicationForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in esydApp.children.filter(expDate = threeMonthDate):

            userEmail = subField.application.foreas.email
            subField =  subField.subField.subField
            regulation = subField.subField.regulation.regulation

            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το Υπουργείο Ανάπτυξης για το θεματικό πεδίο "' + subField + '" της νομοθεσίας "'+ regulation +'" λήγει σε 3 μήνες.',
                    'ypan.info@gmail.com',
                    [userEmail])


    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε',Civil_ExpDate = oneMonthDate): 

        userEmail = ypanApp.foreas.userEmail

        send_mail('Προειδοποίηση Λήξης',
                'Σας υπενθυμίζουμε ότι το ασφαλιστήριο συμβόλαιο αστικής επαγγελματικής ευθύνης που καταθέσατε στην αίτηση σας με αριθμό ' + ypanApp.id + ' στο Υπουργείο Ανάπτυξης λήγει σε 1 μήνα.',
                'ypan.info@gmail.com',
                [userEmail])


    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε',Civil_ExpDate = threeMonthDate):
        
            userEmail = ypanApp.foreas.email

            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι το ασφαλιστήριο συμβόλαιο αστικής επαγγελματικής ευθύνης που καταθέσατε στην αίτηση σας με αριθμό ' + ypanApp.id + ' στο Υπουργείο Ανάπτυξης λήγει σε 3 μήνες.',
                    'ypan.info@gmail.com',
                    [userEmail])

                
