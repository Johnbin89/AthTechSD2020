# Generated by Django 3.0.4 on 2020-05-15 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('applications', '0003_applicationform_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='foreas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
