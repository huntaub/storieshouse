from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.shortcuts import get_object_or_404
import datetime
from django.core.urlresolvers import reverse

from podcast.models import *

# iTunes Podcast Feed Generator
class iTunesPodcastsFeedGenerator(Rss201rev2Feed):

    def rss_attributes(self):
        return {u"version": self._version, u"xmlns:atom": u"http://www.w3.org/2005/Atom", u'xmlns:itunes': u'http://www.itunes.com/dtds/podcast-1.0.dtd'}

    def add_root_elements(self, handler):
        super(iTunesPodcastsFeedGenerator, self).add_root_elements(handler)
        handler.addQuickElement(u'itunes:subtitle', self.feed['subtitle'])
        handler.addQuickElement(u'itunes:author', self.feed['author_name'])
        handler.addQuickElement(u'itunes:summary', self.feed['description'])
        handler.addQuickElement(u'itunes:explicit', self.feed['iTunes_explicit'])
        handler.startElement(u"itunes:owner", {})
        handler.addQuickElement(u'itunes:name', self.feed['iTunes_name'])
        handler.addQuickElement(u'itunes:email', self.feed['iTunes_email'])
        handler.endElement(u"itunes:owner")
        handler.addQuickElement(u'itunes:image', self.feed['iTunes_image_url'])

    def add_item_elements(self,  handler, item):
        super(iTunesPodcastsFeedGenerator, self).add_item_elements(handler, item)
        handler.addQuickElement(u'itunes:summary',item['summary'])
        handler.addQuickElement(u'itunes:duration',item['duration'])
        handler.addQuickElement(u'itunes:explicit',item['explicit'])

class iTunesPodcastPost():
    def __init__(self, podcast):
        self.id = podcast.id
        self.approval_date_time = podcast.data_published
        self.title = podcast.name
        self.number = podcast.number
        self.summary = podcast.show_notes
        self.enclosure_url = podcast.audio
        self.enclosure_length = podcast.length()
        self.enclosure_mime_type = podcast.mime()
        self.duration = 0
        self.explicit = u'yes'
    
    def __unicode__(self):
        return "Podcast: %s" % self.title
    
    def get_absolute_url(self):
        return ('podcast_view', [str(self.id)])

class PodcastFeed(Feed):
    feed_type = iTunesPodcastsFeedGenerator
    iTunes_name = u'StoriesHouse'
    iTunes_email = u'h@hunterleath.com'
    # iTunes_image_url = u'http://example.com/url/of/image'
    iTunes_explicit = u'yes'

    def get_object(self, request, slug):
        self.object = get_object_or_404(Podcast, slug=slug)
        self.iTunes_image_url = self.object.image
        return self.object

    def title(self, obj):
        return obj.name

    def description(self, obj):
        return obj.description

    def link(self, obj):
        return ('http://storieshouse.com/podcast/' + obj.slug)

    def items(self, obj):
        return [iTunesPodcastPost(x) for x in Episode.objects.filter(podcast=obj).order_by('-data_published')]

    def feed_extra_kwargs(self, obj):
        extra = {}
        extra['iTunes_name'] = self.iTunes_name
        extra['iTunes_email'] = self.iTunes_email
        extra['iTunes_image_url'] = self.iTunes_image_url
        extra['iTunes_explicit'] = self.iTunes_explicit
        return extra

    def item_extra_kwargs(self, item):
        return {'summary':item.summary, 'duration':item.duration, 'explicit':item.explicit}

    def item_title(self, item):
        return u'Episode %i: %s' % (item.number, item.title)

    def item_description(self, item):
        return item.show_notes

    def item_link(self, item):
        return ('http://storieshouse.com/podcast/' + self.object.slug + '/' + str(item.number))
    
    def item_pubdate(self, item):
        return item.approval_date_time

    def item_enclosure_url(self, item):
        return item.enclosure_url

    def item_enclosure_length(self, item):
        return item.enclosure_length

    def item_enclosure_mime_type(self, item):
        return item.enclosure_mime_type

    def item_description(self, item):
        return item.summary

    author_name = "StoriesHouse"
    author_link = "http://storieshouse.com"
    feed_copyright = 'Copyright (c) 2013-2014, StoriesHouse'
