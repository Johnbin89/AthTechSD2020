# from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
class ApplicantProfile(models.Model):
    user = models.ForeignKey('auth.User', default=1, on_delete= models.CASCADE)
    companyName = models.CharField(max_length = 250 , verbose_name ='Ονομασία', blank = True)
    distTitle = models.CharField(max_length=100, verbose_name ='Διακριτικός Τίτλος', blank = True)
    afm = models.CharField(max_length= 20, verbose_name ='ΑΦΜ', blank = True)
    doy = models.CharField(max_length= 100, verbose_name ='Δ.Ο.Υ.', blank = True)
    gemi = models.CharField(max_length = 20, verbose_name ='ΓΕΜΗ', blank = True)
    address = models.CharField(max_length = 250, verbose_name ='Διεύθυνση', blank = True)
    postalCode = models.CharField(max_length = 10, verbose_name ='Ταχ. Κώδικας', blank = True)
    phone = models.CharField(max_length = 15, verbose_name ='Τηλέφωνο', blank = True)
    fax = models.CharField(max_length = 15, verbose_name ='Φαξ', blank = True)
    email =models.CharField(max_length = 100, verbose_name ='E-mail')
    contactPerson =models.CharField(max_length = 100, verbose_name ='Πρόσωπο Επικοινωνίας', blank = True)

    def get_absolute_url(self):
        return reverse('profile',args=[self.user.id])

