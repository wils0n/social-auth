from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Photo(models.Model):
    picture = models.ImageField(upload_to='users/pictures/')
    user = models.ForeignKey(User, related_name='fotos')
    is_avatar = models.BooleanField(default=False)


class Perfil(models.Model):
    user = models.OneToOneField(User)

    @property
    def avatar(self):
        foto = None
        for photo in self.user.fotos.all():
            if photo.is_avatar:
                foto = photo.picture
                break

        if foto:
            return foto
        else:
            return settings.STATIC_URL+"img/avatar_default.png"