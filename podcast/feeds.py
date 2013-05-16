from django.contrib.syndication.views import Feed

from podcast.models import *

class StoriesTimeFeed(Feed):
    title = "StoriesTime"
    link = "/"
    description = "Just a couple of people talking about Television and Writing"

    def items(self):
        return Episode.objects.filter(podcast_id=1).order_by('-data_published')[:5]

    def item_title(self, item):
        return u'Episode %i: %s' % (item.number, item.name)

    def item_description(self, item):
        return item.show_notes

    def item_link(self, item):
        return '/'

    def item_enclosure_url(self, item):
        return item.audio

    def item_enclosure_length(self, item):
        return "56857832"

    item_enclosure_mime_type = "audio/mpeg"
