from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'repo.views.index'),
    (r'upload/$', 'repo.views.upload'),
    (r'get/([\w,\W,\-]+)$', 'repo.views.download'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
