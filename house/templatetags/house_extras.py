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

@register.simple_tag
def category_nav():
	c = Category.objects.all()
	output = ""
	for category in c:
		if (category.name == "NONE"):
			continue
		output += "<li><a href='" + cat_url(category) + "'>" + category.name + "</a></li>"
	return output

@register.filter
def cat_url(object):
	if (object == None): 
		return None
	elif (object.name == "NONE"):
		return "#"
	else:
		return ("/category/" + object.name.lower())

@register.inclusion_tag('grid.html')
def story_grid(story_list):
	return {'stories': story_list}