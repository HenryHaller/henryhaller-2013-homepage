from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^.*', 'henryhaller.views.under_construction', name="under_construction"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^permalink/(?P<short_form_url>\S+)/?$', 'henryhaller.views.permalink', name='permalink'),
    url(r'^.*', 'henryhaller.views.home', name='home'),
    # url(r'^django_dir/', include('django_dir.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
