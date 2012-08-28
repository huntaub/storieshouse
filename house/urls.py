from django.conf.urls import patterns, include, url
from house.views import *
from house.models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.site.register(Story)
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'write/$', login_required(StoryCreate.as_view()), name='story_add'),
    url(r'story/$', login_required(StoryList.as_view()), name='story_list'),
    url(r'story/(?P<pk>\d+)/edit/$', login_required(StoryUpdate.as_view()), name='story_update'),
    url(r'story/(?P<pk>\d+)/delete/$', login_required(StoryDelete.as_view()), name='story_delete'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'(?P<user>[-a-z0-9_]+)/(?P<slug>[-a-z0-9_]+)/$', StoryView.as_view(), name="story_view"),
    url(r'(?P<user>[-a-z0-9_]+)/$', UserStoryView.as_view(), name="user_view"),
)
