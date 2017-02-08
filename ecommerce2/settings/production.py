
#static is here mvpland_static
#postgresql -- mvpland
#username -- cfedeploy
#password -- ##


"""
Django settings for ecommerce2 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#root of project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_k&!^if17lw$9pfpeq60^68&@)#%27%hjx3sw(t3)e93mcz6=9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = (
	("Justin", "codingforentrepreneurs@gmail.com"),

	)

ALLOWED_HOSTS = ['multi-ecommerce.herokuapp.com']
#purchasing domain name http://name.com

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yourgmail@gmail.com'
EMAIL_HOST_PASSWORD = 'yourpassword'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

'''
If using gmail, you will need to
unlock Captcha to enable Django
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''



# Application definition


INSTALLED_APPS = (
    #django app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'crispy_forms',
    'registration',
    'django_filters',
	'storages',
    #my apps
    'newsletter',
    'products',
    'carts',
    'orders',
    'sellers',
)

ROOT_URLCONF = 'ecommerce2.urls'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ecommerce2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'ecommerce2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#production deploy postgres
# keep this
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}
# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
#os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")


#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'


#DJANGO REGISTRATION REDUX SETTINGS
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

#BRAINTREE PAYMENTS DETAILS

BRAINTREE_PUBLIC = "6rhmcym3ppvggbrq"
BRAINTREE_PRIVATE = "db78285aa54368a5c299ccf62f0f0530"
BRAINTREE_MERCHAND_ID = "kkj4x5y4nq5msn5r"
BRAINTREE_ENVIRONMENT = "sandbox"


# AWS
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

AWS_S3_SECURE_URLS = True
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True
AWS_ACCESS_KEY_ID = "AKIAJBXGEKRT5MG4ML2A>"
AWS_SECRET_ACCESS_KEY = "AWSSecretKey=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"
AWS_STORAGE_BUCKET_NAME = 'multi-ecommerce'
AWS_S3_CUSTOM_DOMAIN = 's3.amazonaws.com/%s' % AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'src.utils.StaticRootS3BotoStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

DEFAULT_FILE_STORAGE = 'src.utils.MediaRootS3BotoStorage'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

AWS_HEADERS = {
    'x-amz-acl': 'public-read',
    'Cache-Control': 'public, max-age=31556926'
}

import datetime

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
'Expires': expires,
'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
