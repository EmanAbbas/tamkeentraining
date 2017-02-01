"""
Definition of urls for TamkeenDjango.
"""

from django.conf.urls import  include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from tamkeenapp import views
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'TamkeenDjango.views.home', name='home'),

     #,
       url(r'^$', views.home, name='home'),
        url(r'^home$', views.home, name='home'),
        url(r'^services$', TemplateView.as_view(template_name='services.html'), name='services'),
        url(r'^training$', views.Training.as_view(), name='training'),
        url(r'^contact_us$', views.contact, name='contact'),
        url(r'^training/(?P<pk>[0-9]*)$', views.CourseDetail.as_view(), name='course'),
        url(r'^workshop/(?P<pk>[0-9]*)$', views.WorkshopDetail.as_view(), name='workshop'),
        url(r'^certificates$', views.certificates, name='certificates'),
     
     #(r'^tamkeenapp/', include('tamkeenapp.urls')),
    
     #,
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]
