# Generated by Django 3.0.4 on 2020-06-13 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0009_auto_20200611_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationypanform',
            name='Civil_ExpDate',
            field=models.DateField(default=datetime.date.today, verbose_name='Ημ/νία λήξης ασφάλισης'),
        ),
    ]
