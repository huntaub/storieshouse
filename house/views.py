# Create your views here.
from django import forms
from house.models import *
from django.views.generic.detail import DetailView
from django.forms.widgets import TextInput, Textarea

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

class StoryList(ListView):
    template_name = "story_list.html"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Story.objects.all()
        else:
            return Story.objects.filter(user = self.request.user)

class HomePage(ListView):
    template_name = 'base.djt'
    model = Story

    def get_queryset(self):
        stories = Story.objects.filter(published = True)[:5]
        top = stories[0]
        top.viewcount += 1
        top.save()
        return stories

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
        return HttpResponseRedirect('/')

class StoryUpdate(UpdateView):
    model = Story
    form_class = StoryForm
    success_url = '/'

class StoryDelete(DeleteView):
    model = Story
    success_url = '/story/'


class StoryView(DetailView):
    model = Story

    def get_object(self):
        user = User.objects.get(username=self.kwargs['user'])
        story = Story.objects.get(slug = self.kwargs['slug'], user=user, published=True)
        story.viewcount += 1
        story.save()
        return story

class UserStoryView(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        kwargs['stories'] = self.object.story_set.all
        kwargs['profile'] = StoryAuthor.find(self.object)
        kwargs['top_story'] = self.object.story_set.order_by('-viewcount')[0]
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