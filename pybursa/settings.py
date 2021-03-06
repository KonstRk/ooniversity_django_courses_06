"""
Django settings for pybursa project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+wj_g0r9h4&iucqv&ksnrk37393#lz-)#=h3b+*vqoomc(3_39'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quadratic',
    'feedbacks',
    'courses.apps.CoursesConfig',
    'students.apps.StudentsConfig',
    'coaches.apps.CoachesConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pybursa.urls'

TEMPLATES = [
  {'APP_DIRS': True,
  'BACKEND': 'django.template.backends.django.DjangoTemplates',
  'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates/courses'),
           os.path.join(BASE_DIR, 'templates/students'), os.path.join(BASE_DIR, 'quadratic/templates')],
  'OPTIONS': {'context_processors': ['django.template.context_processors.debug',
                                     'django.template.context_processors.request',
                                     'django.contrib.auth.context_processors.auth',
                                     'django.contrib.messages.context_processors.messages']}}]

WSGI_APPLICATION = 'pybursa.wsgi.application'


EMAIL_HOST = "127.0.0.1"
EMAIL_PORT = "1025"

ADMINS = [('John', 'john@example.com'), ('Mary', 'mary@example.com')]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
#]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
            'students_log': {
                'level': 'WARNING',
                'class': 'logging.FileHandler',
                'filename':  os.path.join(BASE_DIR, 'students_logger.log'),
                'formatter': 'students'
            },
            'courses_log': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename':  os.path.join(BASE_DIR, 'courses_logger.log'),
                'formatter': 'courses'
            },
        },
    'loggers': {
        'students': {
            'handlers': ['students_log'],
            'level': 'WARNING',
            'propagate': True,
        },
        'courses': {
            'handlers': ['courses_log'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
    'formatters': {
        'students': {
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(message)s'
        },
        'courses': {
            'format': '%(levelname)s %(message)s'
        }
    }
}