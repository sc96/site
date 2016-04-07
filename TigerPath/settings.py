#Hello World
"""
Django settings for TigerPath project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
#import dj_database_url # this crashes the app! - apr 7
#import os.path
#import django
#django.setup()

#Entered for heroku
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# the next 3 lines also crash the app - apr 7
#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
#STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
#    os.path.join(PROJECT_ROOT, 'static'),
#)
# this also crashes the app - apr 7
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

###########HEROKU END


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b%5tu%(nr6=@t)_mz)3e03ntd$svm!!w6t0mmi-#@4-r=z0xr&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'TigerPath.apps.TigerPathConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cas', ### this was working with me and sam - maybe its heroku?
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cas.middleware.CASMiddleware',
]

ROOT_URLCONF = 'TigerPath.urls'

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

WSGI_APPLICATION = 'TigerPath.wsgi.application'


# CAS Authentication stuff

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'cas.backends.CASBackend',
)

CAS_SERVER_URL = 'http://cast.cs.princeton.edu/'
# CAS_SERVER_URL = 'https://fed.princeton.edu/cas/'

CAS_REDIRECT_URL = '/'

CAS_EMAIL_DOMAIN = 'princeton.edu'

LOGIN_URL = '/login'


# END AUTHENTICATION CONFIGURATION



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nwertz_natalietest',
        'USER': 'nwertz_django',
        'PASSWORD': 'barbecue18',
        'HOST': 'dascpan204l.princeton.edu',
        'PORT': '3306',
    }
}


#Entered for heroku

DATABASES['default'] = dj_database_url.parse('mysql://nwertz_django:barbecue18@dascpan204l.princeton.edu:3306/nwertz_natalietest', conn_max_age=600)
#db_from_env = dj_database_url.config(conn_max_age=500)
#DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

DIRNAME = os.path.dirname(__file__)

STATIC_ROOT = os.path.join(DIRNAME, 'static')

STATIC_URL = '/static/'