from django.conf.urls import patterns, include, url

from podcast.feeds import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storieshouse.views.home', name='home'),

    url(r'^storiestime/feed/$', StoriesTimeFeed()),
)
