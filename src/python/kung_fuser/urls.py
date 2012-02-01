from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'kung_fuser.home.views.index', name='Home'),
    # Examples:
    # url(r'^$', 'kung_fuser.views.home', name='home'),
    # url(r'^kung_fuser/', include('kung_fuser.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
