from django.core.management.base import BaseCommand, CommandError
from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail  
from applications.models import ApplicationYpanForm,ApplicationForm
from django_q.tasks import schedule
import arrow


def run_reminder():
    print('start email reminder')

    oneMonthDate = date.today() + relativedelta(months=1)
    threeMonthDate = date.today() + relativedelta(months=3)
    print(oneMonthDate)
    print(threeMonthDate)

    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in ypanApp.ypan_subfields.filter(expDate = oneMonthDate):
            userEmail = subField.application.foreas.foreas_profile.email
            field =  subField.subField.subField
            regulation = subField.subField.regulation.regulation
            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το Υπουργείο Ανάπτυξης για το θεματικό πεδίο "' + field + '" της νομοθεσίας "'+ regulation +'" λήγει σε 1 μήνα.',
                    '***REMOVED***',
                    [userEmail])

    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in ypanApp.ypan_subfields.filter(expDate = threeMonthDate):

            userEmail = subField.application.foreas.foreas_profile.email
            field =  subField.subField.subField
            regulation = subField.subField.regulation.regulation

            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το Υπουργείο Ανάπτυξης για το θεματικό πεδίο "' + field + '" της νομοθεσίας "'+ regulation +'" λήγει σε 3 μήνες.',
                    '***REMOVED***',
                    [userEmail])


    for esydApp in ApplicationForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in esydApp.children.filter(expDate = oneMonthDate):
            userEmail = subField.application.foreas.foreas_profile.email
            field =  subField.subField.subField
            regulation = subField.subField.regulation.regulation
            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το ΕΣΥΔ για το θεματικό πεδίο "' + field + '" της νομοθεσίας "'+ regulation +'" λήγει σε 1 μήνα.',
                    '***REMOVED***',
                    [userEmail])

    for esydApp in ApplicationForm.objects.filter(status ='Εγκρίθηκε'):

        for subField in esydApp.children.filter(expDate = threeMonthDate):

            userEmail = subField.application.foreas.foreas_profile.email
            field =  subField.subField.subField
            regulation = subField.subField.regulation.regulation

            send_mail('Προειδοποίηση Λήξης',
                    'Σας υπενθυμίζουμε ότι η αναγνώριση σας από το ΕΣΥΔ για το θεματικό πεδίο "' + field + '" της νομοθεσίας "'+ regulation +'" λήγει σε 3 μήνες.',
                    '***REMOVED***',
                    [userEmail])


    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε',Civil_ExpDate = oneMonthDate): 

        userEmail = ypanApp.foreas.foreas_profile.email

        send_mail('Προειδοποίηση Λήξης',
                'Σας υπενθυμίζουμε ότι το ασφαλιστήριο συμβόλαιο αστικής επαγγελματικής ευθύνης που καταθέσατε στην αίτηση σας με αριθμό ' + str(ypanApp.id) + ' στο Υπουργείο Ανάπτυξης λήγει σε 1 μήνα.',
                '***REMOVED***',
                [userEmail])


    for ypanApp in ApplicationYpanForm.objects.filter(status ='Εγκρίθηκε',Civil_ExpDate = threeMonthDate):
        
        userEmail = ypanApp.foreas.foreas_profile.email

        send_mail('Προειδοποίηση Λήξης',
                'Σας υπενθυμίζουμε ότι το ασφαλιστήριο συμβόλαιο αστικής επαγγελματικής ευθύνης που καταθέσατε στην αίτηση σας με αριθμό ' + str(ypanApp.id) + ' στο Υπουργείο Ανάπτυξης λήγει σε 3 μήνες.',
                '***REMOVED***',
                [userEmail])

    print('end email reminder')

def start_email_schedule():
    schedule('applications.reminder.run_reminder',
        name='daily_expDate_check',
        schedule_type='D')

def min_email_schedule():
    schedule('applications.reminder.run_reminder',
        name='minftest_expDate_check',
        schedule_type='I',
        minutes=15)


                
