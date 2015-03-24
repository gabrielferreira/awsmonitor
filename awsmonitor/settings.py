"""
Django settings for awsmonitor project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oz&t&%sx86@ehq-uvf##dhlef9ci$q%9jb!1@ipdbhb7aotif5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'monitor'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'awsmonitor.urls'

WSGI_APPLICATION = 'awsmonitor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# AWS credentials
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

import ipdb; ipdb.set_trace()

# Custom S3 storage backends to store files in subfolders.
from storages.backends.s3boto import S3BotoStorage

MediaRootS3BotoStorage = lambda: S3BotoStorage(location='media')

# Configure to use S3
USE_S3 = False
AWS_STORAGE_BUCKET_NAME = 'bucketname-dev'
AWS_QUERYSTRING_AUTH = False
S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

if USE_S3:
    DEFAULT_FILE_STORAGE = 'myproject.s3utils.MediaRootS3BotoStorage'
    THUMBNAIL_DEFAULT_STORAGE = 'myproject.s3utils.MediaRootS3BotoStorage'
    MEDIA_URL = S3_URL + '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../..',  'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../..', 'static')
