__author__ = 'wilson'

from urllib2 import urlopen
from urllib import urlretrieve

from django.core.files.base import ContentFile, File
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from social.backends.facebook import FacebookOAuth2

from django.conf import settings
#from social_auth.backends.twitter import TwitterBackend
#from social_auth.backends.google import GoogleOAuth2Backend

from auth.models import Photo, Perfil


def get_profile_avatar(strategy, uid, response, user=None, *args, **kwargs):

    url = None

    if kwargs['is_new']:
        if kwargs['backend'].__class__ == FacebookOAuth2:
            url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

        if url:
            try:
                avatar = urlopen(url)
                photo = Photo(user=user, is_avatar=True)
                photo.picture.save(slugify(user.username + " ninja") + ".png", ContentFile(avatar.read()))
                photo.save()

            except:
                avatar = open(settings.STATIC_URL+"img/avatar_default.png", "r+")
                photo = Photo(user=user, is_avatar=True)
                photo.picture.save(slugify(user.username + " ninja") + ".png", ContentFile(avatar.read()))
                photo.save()
        else:
            avatar = open(settings.STATIC_URL+"img/avatar_default.png", "r+")
            photo = Photo(user=user, is_avatar=True)
            photo.picture.save(slugify(user.username + " ninja") + ".png", ContentFile(avatar.read()))
            photo.save()

        try:
            p,n = Perfil.objects.get_or_create(user=user)
        except:
            pass
