from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404

from podcast.models import *

class PodcastFeed(Feed):
    description = "Just a couple of people talking about Television and Writing"

    def get_object(self, request, slug):
        self.object = get_object_or_404(Podcast, slug=slug)
        return self.object

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return ('http://storieshouse.com/podcast/' + obj.slug)

    def items(self, obj):
        return Episode.objects.filter(podcast=obj).order_by('-data_published')

    def item_title(self, item):
        return u'Episode %i: %s' % (item.number, item.name)

    def item_description(self, item):
        return item.show_notes

    def item_link(self, item):
        return ('http://storieshouse.com/podcast/' + self.object.slug + '/' + str(item.number))

    def item_pubdate(self, item):
        return item.data_published

    def item_enclosure_url(self, item):
        return item.audio

    def item_enclosure_length(self, item):
        return item.length()

    def item_enclosure_mime_type(self, item):
        return item.mime()

    author_name = "StoriesHouse"
    author_link = "http://storieshouse.com"
    feed_copyright = 'Copyright (c) 2013-2014, StoriesHouse'
