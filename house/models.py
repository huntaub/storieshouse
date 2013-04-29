from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify

class Category(models.Model):
	name = models.CharField(max_length = 15)
	html_class = models.CharField(max_length = 15)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class StoryAuthor(models.Model):
	user = models.ForeignKey(User)
	about = models.TextField()

	def __unicode__(self):
		return "StoryAuthor: %s" % self.user.username

	@staticmethod
	def find(u):
		author, created = StoryAuthor.objects.get_or_create(user=u)
		return author

# Create your models here.
class Story(models.Model):
	ICON_CHOICES = (
		("bolt", "Lightning Bolt"),
		("road", "Road"),
		("beaker", "Beaker"),
		("globe", "Globe"),
		("cut", "Scissors"),
		("credit-card", "Credit Card"),
		("bell", "Bell"),
		("bullhorn", "Bullhorn"),
		("comment-alt", "Comment"),
		("envelope-alt", "Envelope"),
		("briefcase", "Briefcase"),
		("dashboard", "Dashboard"),
		("cloud", "Cloud"),
		("film", "Film"),
		("headphones", "Headphones"),
		("calendar", "Calendar"),
		("coffee", "Coffee"),
		("leaf", "Leaf"),
		("refresh", "Refresh"),
		("glass", "Martini"),
		("camera-retro", "Camera"),
		("laptop", "Laptop")
	)

	title = models.TextField()
	body = models.TextField()
	icon = models.CharField(max_length = 30, choices = ICON_CHOICES, blank = True, null = True)
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	published = models.BooleanField()
	slug = models.SlugField()
	viewcount = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_added']

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Story, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return ("/" + self.user.username + "/" + self.slug)

	def __unicode__(self):
		return '%s by %s' % (self.title, self.user)