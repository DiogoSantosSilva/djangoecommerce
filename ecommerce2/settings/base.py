
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#root of project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'csqwlmc8s55o($rt6ozh7u+ui9zb-et00w$d90j8$^!nvj41_r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['multi-ecommerce.herokuapp.com']


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'panggolim@gmail.com'
EMAIL_HOST_PASSWORD = 'Di728560@@'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_DEBUG = False

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
    'registration',
    'crispy_forms',
    'django_filters',
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
                #app
                #'products.context_processors.categories'
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce2.wsgi.application'


# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
