# Generated by Django 5.0.2 on 2024-05-04 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0012_auto_20200618_1319'),
        ('django_drf_filepond', '0010_temp_chunked_biginteger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_drf_filepond.storedupload'),
        ),
    ]
