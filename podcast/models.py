from django.db import models

# Create your models here.
class Podcast(models.Model):
	name = models.CharField(max_length=255)
	image = models.URLField()

	def __unicode__(self):
		return self.name

class Episode(models.Model):
	name = models.CharField(max_length=255)
	number = models.IntegerField()
	show_notes = models.TextField()
	audio = models.URLField()
	podcast = models.ForeignKey(Podcast)
	data_published = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s %i: %s' % (self.podcast.name, self.number, self.name)
