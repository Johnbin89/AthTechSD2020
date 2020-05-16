# from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


# from django.contrib.auth.models import BaseUserManager, PermissionsMixin
#
#
# # Create your models here.
# class MyUserManager(BaseUserManager):
#     """
#     A custom user manager to deal with emails as unique identifiers for auth
#     instead of usernames. The default that's used is "UserManager"
#     """
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self._create_user(email, password, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, null=True)
#     is_staff = models.BooleanField(
#         _('staff status'),
#         default=False,
#         help_text=_('Designates whether the user can log into this site.'),
#     )
#     is_active = models.BooleanField(
#         _('active'),
#         default=True,
#         help_text=_(
#             'Designates whether this user should be treated as active. '
#             'Unselect this instead of deleting accounts.'
#         ),
#     )
#     USERNAME_FIELD = 'email'
#     objects = MyUserManager()
#
#     def __str__(self):
#         return self.email
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.email


# Create your models here.
class User(AbstractUser):
    is_foreas = models.BooleanField(default=False)
    is_ypan = models.BooleanField(default=False)
    is_esyd = models.BooleanField(default=False)


class ApplicantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    companyName = models.CharField(max_length=250, verbose_name='Ονομασία', blank=True)
    distTitle = models.CharField(max_length=100, verbose_name='Διακριτικός Τίτλος', blank=True)
    afm = models.CharField(max_length=20, verbose_name='ΑΦΜ', blank=True)
    doy = models.CharField(max_length=100, verbose_name='Δ.Ο.Υ.', blank=True)
    gemi = models.CharField(max_length=20, verbose_name='ΓΕΜΗ', blank=True)
    address = models.CharField(max_length=250, verbose_name='Διεύθυνση', blank=True)
    postalCode = models.CharField(max_length=10, verbose_name='Ταχ. Κώδικας', blank=True)
    phone = models.CharField(max_length=15, verbose_name='Τηλέφωνο', blank=True)
    fax = models.CharField(max_length=15, verbose_name='Φαξ', blank=True)
    email = models.CharField(max_length=100, verbose_name='E-mail')
    contactPerson = models.CharField(max_length=100, verbose_name='Πρόσωπο Επικοινωνίας', blank=True)

    def get_absolute_url(self):
        return reverse('foreas_profile', args=[self.user.id])

    def has_empty_fields(self):
        if (self.companyName == "" or self.distTitle == "" or self.afm =="" or self.doy == "" or self.gemi == "" 
        or self.address == "" or self.postalCode == "" or self.phone == "" or self.fax == "" or self.email == "" 
        or self.contactPerson == ""):
            return True
        else :
            return False

class XeiristisYpourgeiou(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=250, verbose_name='Όνομα', blank=True)
    lastname = models.CharField(max_length=100, verbose_name='Επίθετο', blank=True)
    email = models.EmailField(default=None)
    department = models.CharField(max_length=100, verbose_name='Τμήμα', blank=True)
    desk = models.CharField(max_length=100, verbose_name='Γραφείο')

    def get_absolute_url(self):
        return reverse('profile', args=[self.user.id])


class XeiristisEsyd(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=250, verbose_name='Όνομα', blank=True)
    lastname = models.CharField(max_length=100, verbose_name='Επίθετο', blank=True)
    email = models.EmailField(default=None)
    department = models.CharField(max_length=100, verbose_name='Τμήμα', blank=True)
    desk = models.CharField(max_length=100, verbose_name='Γραφείο')

    def get_absolute_url(self):
        return reverse('profile', args=[self.user.id])


class Regulation(models.Model):
    regulation = models.CharField(max_length=250, verbose_name="Nομοθετικη Διάταξη", unique=True)

    class Meta:
        verbose_name = "Διάταξη"
        verbose_name_plural = "Διατάξεις"
        ordering = ['regulation']

    def __str__(self):
        return self.regulation

    def get_absolute_url(self):
        return reverse('regulation', args=None)


class SubField(models.Model):
    regulation = models.ForeignKey(Regulation, default=1, on_delete=models.CASCADE, related_name='children')
    subField = models.CharField(max_length=250, verbose_name="Υπομέρους Θεματικό Πεδίο")

    class Meta:
        unique_together = ('regulation', 'subField')
        verbose_name = "Πεδίο"
        verbose_name_plural = "Πεδία"
        ordering = ['regulation', 'subField']

    def __str__(self):
        return self.regulation.regulation + ' - ' + self.subField

    def get_absolute_url(self):
        return reverse('regulation', args=None)
