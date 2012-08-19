from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Story(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	user = models.ForeignKey(User)