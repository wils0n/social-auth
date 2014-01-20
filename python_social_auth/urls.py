from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy

from auth.views import LoginView, SecretView
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', LoginView.as_view(), name='view_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('view_login')}, name='logout'),
    url(r'^secret/$', SecretView.as_view(), name='view_secret'), 
    url('', include('social.apps.django_app.urls', namespace='social')), 
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                    {'document_root': settings.MEDIA_ROOT, }),
    )