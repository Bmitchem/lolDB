from django.conf.urls import patterns, include, url
from django.contrib import admin
from riotapibase import views

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'riotapibase.views.index'),
                       url(r'armory/', include('armory.urls')),
                       url(r'rest/', include('RiotRest.urls')),

                       )
