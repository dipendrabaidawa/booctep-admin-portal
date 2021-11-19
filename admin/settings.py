"""
Django settings for admin project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import pymysql

from pathlib import Path
import os
import environ


# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env()

env = environ.Env(
    DEBUG=(bool, False)
)

READ_DOT_ENV_FILE= env.bool('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    environ.Env.read_env()

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

pymysql.install_as_MySQLdb()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

ALLOWED_HOSTS = ["*"]


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'

#EMAIL_HOST_USER = 'daoatkhaiteaiso@gmail.com'
#EMAIL_HOST_PASSWORD = 'daoatkhaiteaiso123'
EMAIL_HOST_USER = 'booctepdotcom2030@gmail.com'

EMAIL_HOST_PASSWORD = 'booctepgmailcom1011'
EMAIL_PORT = 993




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'teacher',
    'student',
    'video',
]

SESSION_COOKIE_AGE = 60 * 60 * 24 * 365 * 5  # set session expire time as 5 years

AUTH_USER_MODEL = 'home.Admin'

AUTHENTICATION_BACKENDS =[
    'django.contrib.auth.backends.ModelBackend'
]

DEFAULT_PASSWORD = 'booctep1011'
DEFAULT_PAGESIZE = 10

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'admin/templates') ],
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

WSGI_APPLICATION = 'admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
   # 'default': {
   #    'ENGINE': 'django.db.backends.mysql',
   #    'NAME': 'dzjq9t85dqv8kckj',
   #    'USER': 'otp2j74kv3w9g03y', # 'root',
   #    'PASSWORD': 'ow5vd8s2bue9y9xt',
   #    'HOST': 'x8autxobia7sgh74.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', #'localhost',   # Or an IP Address that your DB is hosted on
   #    'PORT': '3306',
   #  }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'booctop',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

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

EXPIRE_KEY_LIST = []

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
BASE_URL = 'http://127.0.0.1:8000'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "admin/static"),
)