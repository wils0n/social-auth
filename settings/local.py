__author__ = 'wilson'

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SOCIAL_AUTH_FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'user_birthday']
SOCIAL_AUTH_FACEBOOK_KEY = os.environ['FACEBOOK_KEY_LOCAL']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['FACEBOOK_SECRET_LOCAL']

#SOCIAL_AUTH_TWITTER_EXTENDED_PERMISSIONS = ['email', 'user_birthday']
#SOCIAL_AUTH_TWITTER_KEY = ''
#SOCIAL_AUTH_TWITTER_SECRET = ''