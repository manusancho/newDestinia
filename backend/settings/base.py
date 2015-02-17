"""
Django settings for newDestinia_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

# PATHS
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ls*r392&j5)2e&f^#+h^41n6iyj=)*8=k%0j@ew72_r_dl53xb'


DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'solo',
    'yapsy',
    'backend.apps.siteConfiguration',
    'backend.utils',
    'backend.apps.hotels',
    'backend.apps.offers',
    'backend.apps.providers',
    'backend.apps.giata',
    'backend.apps.openFlights',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'



# DATABASE
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'destinia',
        'USER': 'destinia',
        'PASSWORD': 'destinia',
        'STORAGE_ENGINE': 'MyISAM',
    }
}

DATABASE_OPTIONS = {"init_command": "SET foreign_key_checks = 0;"}



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# STATIC FILES (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# Locations to collect static files from
STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'backend/static'),
)

# Absolute path to the directory where static files should be collected
# Web server is serving files
# from this location
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "public/static"))

# URL prefix for static files
STATIC_URL = "/public/static/"


# TEMPLATES
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "public/static/templates/admin"),
    os.path.join(BASE_DIR, "backend/apps/hotels/tpl/"),
    os.path.join(BASE_DIR, "backend/apps/offers/tpl/"),
)

