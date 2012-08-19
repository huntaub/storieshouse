from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Story(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	user = models.ForeignKey(User)
	published = models.BooleanField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s by %s' % (self.title, self.user)