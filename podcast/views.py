# Create your views here.

from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from podcast.models import *

class PodcastHome(TemplateView):
    template_name="podcast/home.html"

    def get_context_data(self, **kwargs):
        context = super(PodcastHome, self).get_context_data(**kwargs)
        context['podcasts'] = Podcast.objects.all()
        return context

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