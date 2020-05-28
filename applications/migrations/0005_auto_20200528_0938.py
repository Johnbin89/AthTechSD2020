# Generated by Django 3.0.4 on 2020-05-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20200516_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='file',
            field=models.FileField(upload_to='applications/static/esyd_files'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='status',
            field=models.CharField(choices=[('Σε εκκρεμότητα', 'Σε εκκρεμότητα'), ('Απορρίφθηκε', 'Απορρίφθηκε'), ('Εγκρίθηκε', 'Εγκρίθηκε')], default='Σε εκκρεμότητα', max_length=30, verbose_name='Κατασταση'),
        ),
        migrations.AlterField(
            model_name='applicationsubfield',
            name='status',
            field=models.CharField(choices=[('Σε εκκρεμότητα', 'Σε εκκρεμότητα'), ('Απορρίφθηκε', 'Απορρίφθηκε'), ('Εγκρίθηκε', 'Εγκρίθηκε')], default='Σε εκκρεμότητα', max_length=30, verbose_name='Κατάσταση'),
        ),
    ]
