"""
Definition of urls for TamkeenDjango.
"""

from django.conf.urls import patterns, include, url

from django.views import defaults
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


#urlpatterns = patterns('myproject.myapp.views',
#    (r'^$', 'default_view',
#    (r'^something/$', 'something_view',
#)
urlpatterns = patterns('TamkeenDjango.tamkeenapp.views',
    # Examples:
    url(r'^$', 'tamkeenapp.views.home', name='home')
    
     #,

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
