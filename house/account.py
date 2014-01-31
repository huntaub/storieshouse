from django.views.generic import TemplateView
from house.models import *
from datetime import datetime, timedelta

class AccountDashboard(TemplateView):
    template_name = 'house_admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDashboard, self).get_context_data(**kwargs)
        context['stories'] = Story.objects.filter(user=self.request.user).order_by("-date_added")
        now = datetime.now()
        lastweek = now - timedelta(weeks=1)
        context['views'] = [self.request.user.hit_set.filter(date__lt=(now-timedelta(days=x)), date__gt=(now-timedelta(days=x+1))) for x in range(7)]
        context['total_views'] = Hit.objects.filter(author=self.request.user).count()
        context['total_stories'] = context['stories'].count()
        context['top_stories'] = Story.top_by_author(5, self.request.user, lastweek)
        return context