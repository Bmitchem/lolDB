__author__ = 'bob'
from django.conf.urls import patterns, include, url
from armory import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'RiotProject.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^champion/$', views.champion, name='champ_id'),

                       url(r'^champion_search/$', views.champion_search, name='suggestion'),
                       url(r'^player_search/$', views.player_search, name='suggestion'),
                       url(r'^match_specific_data/$', views.match_info_update, name='match'),
                       )
