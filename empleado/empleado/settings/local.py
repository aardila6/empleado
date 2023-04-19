from .base import *
import os
import sys
from django.conf import settings
from django.conf.urls.static import static

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'alfonso',
        'PASSWORD': 'servi15',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [str(BASE_DIR / 'static')]
MEDIA_URL = '/media/'
#MEDIA_ROOT = BASE_DIR.child('media')

#STATICFILES_DIRS = [
#    BASE_DIR / "static",
#]
STATIC_URL = 'static/'
