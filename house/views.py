# Create your views here.
from django import forms
from house.models import *
from podcast.models import *
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.forms.widgets import TextInput, Textarea
from django.db.models import Q
from django.core.urlresolvers import reverse

class StoryForm(forms.ModelForm):
    title = forms.CharField(widget = TextInput(attrs = {'style': 'width: 500px'}))
    body = forms.CharField(widget = Textarea(attrs = {'style': 'width: 500px'}))
    class Meta:
        model = Story
        exclude = ('user', 'date_added', 'slug', 'viewcount')

class StoryAuthorForm(forms.ModelForm):
    about = forms.CharField(widget = Textarea(attrs = {'style': 'width: 500px'}))
    class Meta:
        model = StoryAuthor
        exclude = ('user')


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.http import HttpResponseRedirect

class HomePage(TemplateView):
    template_name = 'base.html'
    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['media_list'] = Episode.objects.order_by("-date_published")
        context['featured_stories'] = Story.objects.filter(published=True).order_by("-date_added")[:2]
        context['all_stories'] = Story.objects.filter(published=True).order_by("-date_added")[2:]
        return context

class StoryView(DetailView):
    model = Story
    template_name = 'house/story_detail.html'

    # def get_template_names(self):
    #     if not self.object.image:
    #         return 'house/story_old.html'
    #     else:
    #         return 'house/story_detail.html'

    def get_object(self):
        user = User.objects.get(username=self.kwargs['user'])
        current_user = self.request.user
        if current_user.is_authenticated():
            current_user = current_user.pk
        else:
            current_user = 0
        story = Story.objects.get(Q(slug = self.kwargs['slug'], user=user.pk), Q(published=True) | Q(published=False, user=current_user))
        story.viewcount += 1
        story.save()
        return story

class StoryList(ListView):
    template_name = "story_list.html"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Story.objects.all()
        else:
            return Story.objects.filter(user = self.request.user)

class StoryCreate(CreateView):
    model = Story
    form_class = StoryForm

    def form_valid(self, form):
        s = Story()
        s.title = form.cleaned_data['title']
        s.body = form.cleaned_data['body']
        s.published = form.cleaned_data['published']
        s.icon = form.cleaned_data['icon']
        s.category = form.cleaned_data['category']
        s.viewcount = 0
        s.user = self.request.user
        s.save()
        return HttpResponseRedirect(reverse('story_view', kwargs={'slug':s.slug, 'user':s.user}))

class StoryUpdate(UpdateView):
    model = Story
    form_class = StoryForm
    success_url = '/'

    def get_success_url(self):
        return reverse('story_view', kwargs={'slug':self.object.slug, 'user':self.object.user}) 

class StoryDelete(DeleteView):
    model = Story
    success_url = '/story/'

class UserStoryView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        kwargs['stories'] = self.object.story_set.filter(published=True)
        kwargs['profile'] = StoryAuthor.find(self.object)
        kwargs['top_stories'] = self.object.story_set.filter(published=True).order_by('-viewcount')[0:3]
        return super(UserStoryView, self).get_context_data(**kwargs)

    def get_object(self):
        self.object = User.objects.get(username=self.kwargs['pk'])
        return self.object

class AuthorUpdate(UpdateView):
    model = StoryAuthor
    form_class = StoryAuthorForm
    success_url = "/"

    def get_object(self):
        return StoryAuthor.find(self.request.user)

class CategoryView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        kwargs['top_story'] = self.object.story_set.order_by('-viewcount')[:3]
        return super(CategoryView, self).get_context_data(**kwargs)

    def get_object(self):
        self.object = Category.objects.get(name__iexact=self.kwargs['name'])
        return self.object

from django.contrib.syndication.views import Feed

class LatestEntriesFeed(Feed):
    title = "Latest Entries from StoriesHouse.com"
    link = "http://storieshouse.com/"
    description = "We are a group of authors who are looking to share our perspective on the world."

    def items(self):
        return Story.objects.filter(published=True).order_by("-date_added")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body
