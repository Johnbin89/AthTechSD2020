"""
Django settings for certwebapp project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import dotenv
from django.contrib.messages import constants as messages
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#dotenv_file = os.path.join(BASE_DIR, ".env")
#if os.path.isfile(dotenv_file):
#    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '***REMOVED***'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django_q',
    'app',
    'accounts',
    'reporting',
    'applications.apps.ApplicationsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'background_task',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'certwebapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'certwebapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#DATABASES = {}
#DATABASES['default'] = dj_database_url.config(conn_max_age=600)
DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'd7hc7das2ffsfc',

        'USER': 'mjpapqhyrrckcn',

        'PASSWORD': '5b9d98962247fc567b39b967e9eea2c253505ebd8af59b3a4f342a0994470060',

        'HOST': 'ec2-176-34-123-50.eu-west-1.compute.amazonaws.com',

        'PORT': '5432',

    }

}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
'''
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'accounts/static',
    'applications/static',
]
'''
AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'user_home_page'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

MEDIA_URL = '***REMOVED***/'
MEDIA_ROOT = '***REMOVED***'
DEFAULT_FILE_STORAGE = '***REMOVED***'
FTP_STORAGE_LOCATION = '***REMOVED***'
#FILE_UPLOAD_TEMP_DIR = '***REMOVED***/tmp'
DATA_UPLOAD_MAX_MEMORY_SIZE = None


django_heroku.settings(locals())
#del DATABASES['default']['OPTIONS']['sslmode']


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '***REMOVED***'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = '***REMOVED***'
EMAIL_HOST_PASSWORD = '***REMOVED***'

Q_CLUSTER = {
    'name': 'django_q_django',
    'workers': 8,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'redis': {
        'host': '***REMOVED***',
        'port': 6379,
        'password': '***REMOVED***',
        'db': 0, }
}