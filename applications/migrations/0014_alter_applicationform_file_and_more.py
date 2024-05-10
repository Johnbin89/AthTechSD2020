# Generated by Django 5.0.2 on 2024-05-08 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0013_alter_applicationform_file'),
        ('django_drf_filepond', '0010_temp_chunked_biginteger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='file',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Art_Of_Incorporation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='art_ink_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Balance_Sheet_3Y',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bal_sheet_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Civil_ID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='civil_id_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Coord_Group_Decl',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cord_group_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Foreign_Activity_Decl',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='for_act_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='GEMI_Cert',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gemi_cert_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='GEMI_NoMod_Cert',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gemi_nomod_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Insurance_Liability_Cert',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ins_lia_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Non_Bankruptcy_Cert_1',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='non_bank_app_1', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Non_Bankruptcy_Cert_2',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='non_bank_app_2', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Non_Clearance_Cert',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='non_clear_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Non_Force_Arrange_Cert',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='non_forge_app', to='django_drf_filepond.storedupload'),
        ),
        migrations.AlterField(
            model_name='applicationypanform',
            name='Tax_Clear_Cert',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tax_clear_app', to='django_drf_filepond.storedupload'),
        ),
    ]