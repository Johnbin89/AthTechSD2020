# Generated by Django 3.0.4 on 2020-05-15 21:10

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_foreas', models.BooleanField(default=False)),
                ('is_ypan', models.BooleanField(default=False)),
                ('is_esyd', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regulation', models.CharField(max_length=250, unique=True, verbose_name='Nομοθετικη Διάταξη')),
            ],
            options={
                'verbose_name': 'Διάταξη',
                'verbose_name_plural': 'Διατάξεις',
                'ordering': ['regulation'],
            },
        ),
        migrations.CreateModel(
            name='ApplicantProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('companyName', models.CharField(blank=True, max_length=250, verbose_name='Ονομασία')),
                ('distTitle', models.CharField(blank=True, max_length=100, verbose_name='Διακριτικός Τίτλος')),
                ('afm', models.CharField(blank=True, max_length=20, verbose_name='ΑΦΜ')),
                ('doy', models.CharField(blank=True, max_length=100, verbose_name='Δ.Ο.Υ.')),
                ('gemi', models.CharField(blank=True, max_length=20, verbose_name='ΓΕΜΗ')),
                ('address', models.CharField(blank=True, max_length=250, verbose_name='Διεύθυνση')),
                ('postalCode', models.CharField(blank=True, max_length=10, verbose_name='Ταχ. Κώδικας')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Τηλέφωνο')),
                ('fax', models.CharField(blank=True, max_length=15, verbose_name='Φαξ')),
                ('email', models.CharField(max_length=100, verbose_name='E-mail')),
                ('contactPerson', models.CharField(blank=True, max_length=100, verbose_name='Πρόσωπο Επικοινωνίας')),
            ],
        ),
        migrations.CreateModel(
            name='XeiristisEsyd',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(blank=True, max_length=250, verbose_name='Όνομα')),
                ('lastname', models.CharField(blank=True, max_length=100, verbose_name='Επίθετο')),
                ('email', models.EmailField(default=None, max_length=254)),
                ('department', models.CharField(blank=True, max_length=100, verbose_name='Τμήμα')),
                ('desk', models.CharField(max_length=100, verbose_name='Γραφείο')),
            ],
        ),
        migrations.CreateModel(
            name='XeiristisYpourgeiou',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(blank=True, max_length=250, verbose_name='Όνομα')),
                ('lastname', models.CharField(blank=True, max_length=100, verbose_name='Επίθετο')),
                ('email', models.EmailField(default=None, max_length=254)),
                ('department', models.CharField(blank=True, max_length=100, verbose_name='Τμήμα')),
                ('desk', models.CharField(max_length=100, verbose_name='Γραφείο')),
            ],
        ),
        migrations.CreateModel(
            name='SubField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subField', models.CharField(max_length=250, unique=True, verbose_name='Υπομέρους Θεματικό Πεδίο')),
                ('regulation', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='accounts.Regulation')),
            ],
            options={
                'verbose_name': 'Πεδίο',
                'verbose_name_plural': 'Πεδία',
                'ordering': ['subField'],
            },
        ),
    ]