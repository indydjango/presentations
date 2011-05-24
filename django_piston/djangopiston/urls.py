from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource
from api.handlers import NewsItemHandler

# NOTE: this is a custom resource to allow remote POST (bypasses django csrf checking)
class CsrfExemptResource(Resource):
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)

newsitem_handler = CsrfExemptResource(NewsItemHandler)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangopiston.views.home', name='home'),
    # url(r'^djangopiston/', include('djangopiston.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/$', newsitem_handler),
    url(r'^news/(\d+)/$', newsitem_handler),
)
