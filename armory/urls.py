__author__ = 'bob'
from django.conf.urls import patterns, include, url
from armory import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RiotProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^champion/(?P<champion_id>\w+)/$', views.champion),

)
