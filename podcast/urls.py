from django.conf.urls import patterns, include, url

from podcast.feeds import *
from podcast.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storieshouse.views.home', name='home'),

    url(r'^storiestime/feed/$', StoriesTimeFeed()),

    url(r'^(?P<slug>\w+)/$', PodcastView.as_view(), name='view_podcast'),
    url(r'^(?P<slug>\w+)/(?P<epi>\d+)/$', EpisodeView.as_view(), name='view_episode'),
)
