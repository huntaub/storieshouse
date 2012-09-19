# Create your views here.
from django import forms
from house.models import *
from django.forms.widgets import TextInput

class StoryForm(forms.ModelForm):
    title = forms.CharField(widget = TextInput(attrs = {'style': 'width: 500px'}))
    class Meta:
        model = Story
        exclude = ('user', 'date_added', 'slug')


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
        return Story.objects.filter(published = True)[:5]

class StoryCreate(CreateView):
    model = Story
    form_class = StoryForm

    def form_valid(self, form):
        s = Story()
        s.title = form.cleaned_data['title']
        s.body = form.cleaned_data['body']
        s.published = form.cleaned_data['published']
        s.icon = form.cleaned_data['icon']
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


class StoryView(HomePage):
    def get_queryset(self):
        user = User.objects.get(username=self.kwargs['user'])
        return Story.objects.filter(slug = self.kwargs['slug'], user=user, published=True)

class UserStoryView(HomePage):
    def get_queryset(self):
        return Story.objects.filter(user = User.objects.get(username=self.kwargs['user']), published=True)