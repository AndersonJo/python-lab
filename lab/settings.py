"""
Django settings for PythonLabDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


ADMINS = (
  ('admin', 'a141890@gmail.com'),
    # ('Your Name', 'your_email@example.com'),
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hr3ti&d6pwb#9c68pez(wuh-2icvyix+vgh52h)u$yj_g93g$r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
MINIFY_505_ON_AJAX = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mket_css',
    'mket_jscript',

    'lab_board',
    'lab_member',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lab.urls'

WSGI_APPLICATION = 'lab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# Set Database
DATABASES = {
     'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'. #django.db.backends.postgresql_psycopg2
        'NAME': 'hbilab',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'hbilab',
        'PASSWORD': '1234',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',  # Set to empty string for default.
        }
}



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Mket Libraries
    os.path.join(BASE_DIR,  'mket_jscript/templates'),
    os.path.join(BASE_DIR,  'mket_css/templates'),

    # Lab
    os.path.join(BASE_DIR,  'lab/templates'),
    os.path.join(BASE_DIR,  'lab_board/templates'),
    os.path.join(BASE_DIR,  'lab_member/templates'),
)