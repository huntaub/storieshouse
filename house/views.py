# Create your views here.
from django import forms
from house.models import *
from podcast.models import *
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.forms.widgets import *
from django.db.models import Q
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta

class StoryForm(forms.ModelForm):
    title = forms.CharField(widget = TextInput(attrs = {'class': 'form-control'}))
    body = forms.CharField(widget = Textarea(attrs = {'class': 'form-control'}))
    class Meta:
        model = Story
        exclude = ('user', 'date_added', 'slug', 'viewcount')
        widgets = {
            'icon': Select(attrs = {'class': 'form-control'}),
            'image': TextInput(attrs = {'class': 'form-control', 'placeholder': 'Use icon for story.'}),
            'category': Select(attrs = {'class': 'form-control'}),
            # 'published': CheckboxInput(attrs = {'class': 'form-control'}),
        }

class StoryAuthorForm(forms.ModelForm):
    about = forms.CharField(widget = Textarea(attrs = {'class': 'form-control'}))
    avatar = forms.CharField(widget = TextInput(attrs = {'class': 'form-control'}))
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
        context['featured_episode'] = Episode.objects.order_by("-data_published")[0]
        context['featured_stories'] = Story.objects.filter(published=True).order_by("-date_added")[:2]
        context['all_stories'] = Story.objects.filter(published=True).order_by("-date_added")[2:7]
        lastweek = datetime.now() - timedelta(weeks=1)
        context['top_users'] = StoryAuthor.top(3, lastweek)
        context['top_stories'] = Story.top(3, lastweek)
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
        # story.viewcount += 1
        story.register_hit()
        story.save()
        return story

class StoryList(ListView):
    template_name = "story_list.html"

    def get_queryset(self):
        return Story.objects.filter(published=True)

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
    template_name = "house_admin/storyauthor_form.html"

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