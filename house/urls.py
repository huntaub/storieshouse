from django.conf.urls import patterns, include, url
from house.views import *
from house.account import *
from house.models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    url(r'^$', HomePage.as_view(), name='home'),

    # url(r'^write/$', login_required(StoryCreate.as_view()), name='story_add'),

    url(r'^stories/$', StoryList.as_view(), name='story_list'),
    # url(r'^stories/(?P<pk>\d+)/edit/$', login_required(StoryUpdate.as_view()), name='story_update'),
    url(r'^stories/(?P<pk>\d+)/delete/$', login_required(StoryDelete.as_view()), name='story_delete'),

    # url(r'category/(?P<name>[-a-z0-9_]+)/$', CategoryView.as_view(), name='category_view'),

	# url(r'feeds/latest/$', LatestEntriesFeed()),

    url(r'^account/settings/$', login_required(AuthorUpdate.as_view()), name='author_update'),
    url(r'^account/dashboard/$', login_required(AccountDashboard.as_view()), name='dashboard'),

    url(r'^account/stories/$', login_required(AccountStories.as_view()), name='admin_story_list'),
    url(r'^account/stories/write/$', login_required(StoryCreate.as_view()), name='story_add'),
    url(r'^account/stories/(?P<pk>\d+)/edit/$', login_required(StoryUpdate.as_view()), name='story_edit'),
    url(r'^account/stories/(?P<pk>\d+)/delete/$', login_required(AccountDashboard.as_view()), name='story_delete'),

    url(r'^(?P<user>[-a-z0-9_]+)/(?P<slug>[-a-z0-9_]+)/$', StoryView.as_view(), name="story_view"),
    url(r'^(?P<pk>[-a-z0-9_]+)/$', UserStoryView.as_view(), name="user_view"),

)
