# Generated by Django 3.0.4 on 2020-05-15 21:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20200516_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationform',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Ημ/νία υποβολής'),
        ),
    ]
