from django.views.generic import TemplateView
from house.models import *
from house.views import StoryForm
from datetime import datetime, timedelta

class AccountDashboard(TemplateView):
    template_name = 'house_admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDashboard, self).get_context_data(**kwargs)
        now = datetime.now()
        lastweek = now - timedelta(weeks=1)
        context['stories'] = Story.objects.filter(user=self.request.user).order_by("-date_added")
        context['views'] = [self.request.user.hit_set.filter(date__lt=(now-timedelta(days=x)), date__gt=(now-timedelta(days=x+1))) for x in range(7)]
        context['total_views'] = Hit.objects.filter(author=self.request.user).count()
        context['total_stories'] = context['stories'].count()
        context['top_stories'] = Story.top_by_author(5, self.request.user, lastweek)
        return context

class AccountStories(TemplateView):
    template_name = 'house_admin/story_list.html'

    def get_context_data(self, **kwargs):
        context = super(AccountStories, self).get_context_data(**kwargs)
        context['stories'] = Story.objects.filter(user=self.request.user).order_by("-date_added")
        return context

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class StoryCreate(CreateView):
    model = Story
    form_class = StoryForm
    template_name = "house_admin/story_form.html"

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
    template_name = 'house_admin/story_form.html'

    def get_success_url(self):
        return reverse('story_view', kwargs={'slug':self.object.slug, 'user':self.object.user}) 