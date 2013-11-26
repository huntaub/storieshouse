from django import template
from house.models import *
from django.template.defaultfilters import wordcount

register = template.Library()

@register.filter
def full_name(object):
	return "%s %s" % (object.first_name, object.last_name)

@register.filter
def drafts(object):
	return Story.objects.filter(published = False, user = object)

@register.filter
def reading_time(object):
	return wordcount(object)/250

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

@register.inclusion_tag('house/list_horizontal_stories.html')
def horizontal_stories(story_list, user=None):
	return {'stories': story_list, 'user': user}

@register.inclusion_tag('story_render.html')
def story_render(story):
	return {'story': story}

# def to_months(story_list):
# 	output = []
# 	current_month = {'name': 'n', 'content': []}
# 	for story in story_list:
# 		if current_month.name == 'n':
# 			current_month.name = story.date_added