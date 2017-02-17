try:
    from base import *
except ImportError:
    pass



import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_k&!^if17lw$9pfpeq60^68&@)#%27%hjx3sw(t3)e93mcz6=9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['multi-ecommerce.herokuapp.com']
#purchasing domain name http://name.com

# Database
	# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

from .db_password import DBPASS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "panggolim",
        'USER': "diogo",
        'PASSWORD': DBPASS,
}
}
# add this
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

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
