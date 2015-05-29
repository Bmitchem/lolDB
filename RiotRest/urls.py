from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'matchhistory/$', view='RiotRest.views.MatchRequest'),

                       )