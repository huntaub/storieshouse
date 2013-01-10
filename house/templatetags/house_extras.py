from django import template
from house.models import *

register = template.Library()

@register.filter
def full_name(object):
	return "%s %s" % (object.first_name, object.last_name)

@register.filter
def drafts(object):
	return Story.objects.filter(published = False, user = object)

@register.simple_tag
def total_users():
	return User.objects.all().count()

@register.simple_tag
def total_stories():
	return Story.objects.all().count()