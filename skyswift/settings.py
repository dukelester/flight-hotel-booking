"""
Django settings for skyswift project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = config('DEBUG')
# DEBUG = False
DEBUG = True

# ALLOWED_HOSTS = ['52.188.149.113', 'ab0be84fbda5.ngrok.io','localhost','127.0.0.1', 'sky-swift.com', 'www.sky-swift.com']
ALLOWED_HOSTS = ['hotel-flight-booking-engine.herokuapp.com', '127.0.0.1']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homepage',
    'hotels',
    # 'flights',
    'cloudinary',
    'ckeditor',
    'userprofile',
    'authentication',
    # 'django_email_verification',
    # 'django_filters',
    'book',
    'flocash',
    'rest_framework',

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
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #     'django.middleware.cache.UpdateCacheMiddleware',
    #    'django.middleware.common.CommonMiddleware',
    #    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'skyswift.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),

                 ],
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

WSGI_APPLICATION = 'skyswift.wsgi.application'

WEBHOOK_EVENTS = (
    "payment.paid",
    "payment.cancelled",
    "payment.refunded",
    "payment.fulfilled"
)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'skyswift',
#         'PASSWORD': 'skyswiftadmin',
#         'USER' :'skyswiftadmin',
#         'PORT':'5432',
#         'HOST':'localhost',
#
#    }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [

    os.path.join(BASE_DIR, 'static'),

]
LOGOUT_REDIRECT_URL = '/'

# cloudinary





SITE_ID = 1

LOGIN_REDIRECT_URL = "loginpage"
LOGOUT_REDIRECT_URL = 'loginpage'
LOGIN_URL = '/'

# THE WSGI THING
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# settins added for sending email


GP_CLIENT_ID = '531500489026-g3viamb559lk34e8p9k09vfssqilphni.apps.googleusercontent.com'
GP_CLIENT_SECRET = 'DjnZspW17akSQr3M9JslPbLB'

AMADEUS_CLIENT_ID = config('AMADEUS_CLIENT_ID')

AMADEUS_CLIENT_SECRET = config('AMADEUS_CLIENT_SECRET')

AUTH_PROFILE_MODULE = 'homepage.Profile'
#
# CACHES = {
#    'default': {
#       'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#       'LOCATION': '/var/tmp/django_cache',
#    }
# }
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }
#
# CACHE_MIDDLEWARE_ALIAS='mycache'
# CACHE_MIDDLEWARE_SECONDS ='3600'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }

MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR, 'media'))

MEDIA_URL = '/media/'

#
# SENDGRID_API_KEY = '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'
#
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = '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'
# EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True



SENDGRID_API_KEY = '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'
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_SANDBOX_MODE_IN_DEBUG = False


EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'info@sky-swift.com'

