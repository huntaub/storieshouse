from django import template
from house.models import *

register = template.Library()

@register.filter
def drafts(object):
	return Story.objects.filter(published = False, user = object)