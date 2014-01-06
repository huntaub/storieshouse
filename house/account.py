from django.views.generic import TemplateView
from house.models import *

class AccountDashboard(TemplateView):
    template_name = 'house_admin/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(AccountDashboard, self).get_context_data(**kwargs)
        context['stories'] = Story.objects.filter(user=self.request.user).order_by("-date_added")
        return context