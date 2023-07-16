"""
Django settings for al_kadome_api project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&&bx=io$y+jl6^g-hl%%c1@3rxvb5)mr7q)v+c%x!4g(dkd&o3"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'storages',
    'corsheaders',
    "category",
    "product",
    "subcategory"
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware'
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000',
    'http://127.0.0.1:3001',    
]

ROOT_URLCONF = "al_kadome_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "al_kadome_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



# AWS_ACCESS_KEY_ID = 'AKIARMPIGDYYHJARES5F'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'alkadome'
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
# AWS_S3_REGION_NAME = 'eu-north-1'
# AWS_DEFAULT_ACL = 'public-read' 
# AWS_S3_OBJECT_PARAMETERS = { 
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
# AWS_S3_FILE_OVERWRITE = False
# AWS_HEADERS = {
#     'Access-Control-Allow-Origin': '*'
# }
# AWS_QUERYSTRING_AUTH = False
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = 'static/' 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# DEFAUKT_FILE_STORAGE = 'storages.backends.filebased.FileBasedStorage'
# FIREBASE_STORAGE_BUCKET = 'alkadome.appspot.com'



import firebase_admin
import os
from firebase_admin import credentials




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_FILE_STORAGE = 'django_firebase.storage.FirebaseStorage'
FIREBASE_STORAGE_BUCKET = 'al-kadome-storage.appspot.com'

FIREBASE_CERT_DATA = os.path.join(BASE_DIR, 'al-kadome-storage-firebase-adminsdk-okghq-abcca6b729.json')
cred = credentials.Certificate(FIREBASE_CERT_DATA)
firebase_admin.initialize_app(cred, { 
    'storageBucket': FIREBASE_STORAGE_BUCKET
})

