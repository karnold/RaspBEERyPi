from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RaspBEERyPi.views.home', name='home'),
    # url(r'^RaspBEERyPi/', include('RaspBEERyPi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {"template": "index.html"}),
    url(r'^current-reading/$', 'beer.views.current_reading'),
)
