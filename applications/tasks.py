import random
from celery import shared_task
from django.core.mail import send_mail 


@shared_task
def send_celery_email(subject, message, sender, recipients):
    send_mail(subject, message, sender, recipients)
    return subject #a return to see at celery results backend. For this in django_db



#Demo Tasks --
@shared_task
def add(x, y):
    # Celery recognizes this as the `applications.tasks.add` task
    # the name is purposefully omitted here.
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # Celery recognizes this as the `sum_list_numbers` task
    return sum(numbers)
#Demo Tasks --

