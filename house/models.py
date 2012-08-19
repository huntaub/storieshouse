from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

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
	)

	title = models.CharField(max_length = 100)
	body = models.TextField()
	icon = models.CharField(max_length = 30, choices = ICON_CHOICES, blank = True, null = True)
	user = models.ForeignKey(User)
	published = models.BooleanField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date_added']

	def __unicode__(self):
		return '%s by %s' % (self.title, self.user)