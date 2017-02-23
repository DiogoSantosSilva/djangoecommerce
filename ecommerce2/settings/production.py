from ecommerce2.settings.base import *
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_k&!^if17lw$9pfpeq60^68&@)#%27%hjx3sw(t3)e93mcz6=9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ADMINS = (
	("diogo", "diogo.ds62@gmail.com"),

	)

ALLOWED_HOSTS = ['multi-ecommerce.herokuapp.com']
#purchasing domain name http://name.com

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'panggolim@gmail.com'
EMAIL_HOST_PASSWORD = 'Di728560@@'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

'''
If using gmail, you will need to
unlock Captcha to enable Django
to  send for you:
https://accounts.google.com/displayunlockcaptcha
'''




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
	'allauth',
    'allauth.account',
    'allauth.socialaccount',
	'smart_selects'
    'django_filters',
    'storages',
     #my apps
    'newsletter',
    'products',
    'carts',
    'orders',
    'sellers',
 )

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

ROOT_URLCONF  = 'ecommerce2.urls'

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
                #app
                #'products.context_processors.categories'
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

WSGI_APPLICATION = 'ecommerce2.wsgi.application'
# Database
	# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# add this
db_from_venv = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_venv)

SECURE_PROXY_SSL_HEADER  =  ('HTTP_X_FORWARDED_PROTO', 'https')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)

#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'


#BRAINTREE PAYMENTS DETAILS

BRAINTREE_PUBLIC = "6rhmcym3ppvggbrq"
BRAINTREE_PRIVATE = "db78285aa54368a5c299ccf62f0f0530"
BRAINTREE_MERCHAND_ID = "kkj4x5y4nq5msn5r"
BRAINTREE_ENVIRONMENT = "sandbox"


# AWS
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'


AWS_ACCESS_KEY_ID = "AKIAJBXGEKRT5MG4ML2A"
AWS_SECRET_ACCESS_KEY = "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"

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'ecommerce2.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'ecommerce2.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'multi-ecommerce'
S3DIRECT_REGION = 'us-west-2'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

import datetime

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    'Expires': expires,
    'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}


SITE_ID = 1

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = None

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_EMAIL_SUBJECT_PREFIX = "My subject: "
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"

ACCOUNT_LOGOUT_ON_GET = False
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SIGNUP_FORM_CLASS = None
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION  = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USERNAME_MIN_LENGTH = 5
ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False
ACCOUNT_PASSWORD_MIN_LENGTH = 6
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
