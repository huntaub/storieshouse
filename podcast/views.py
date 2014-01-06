# Create your views here.

from django.views.generic.detail import DetailView
from podcast.models import *

class PodcastView(DetailView):
	model=Podcast

	def get_object(self, queryset=None):
		slug = self.kwargs['slug']
		return Podcast.objects.get(slug=slug)

class EpisodeView(DetailView):
	model=Episode

	def get_object(self, queryset=None):
		slug = self.kwargs['slug']
		pid = Podcast.objects.get(slug=slug).id
		number = self.kwargs['epi']
		return Episode.objects.get(number=number, podcast_id=pid)