from django.db import models
import django.utils.timezone

# Create your models here.

class BlogPost(models.Model):
	pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length=500)
	text = models.TextField()
	url_title = models.CharField(max_length=350)
	def __unicode__(self): return self.title
	def pretty_age(self):
		age_diff = django.utils.timezone.now() - self.pub_date
		days, seconds = age_diff.days, age_diff.seconds
		if days == 0 and seconds < 60: return "less than 1 minute old"
		if days == 0 and seconds < 3600: return "less than1 hour old"
		if days == 0 and seconds < (24 * 60 * 60): return "less than 1 day old"
		if days == 1: return "1 day old"
		return str(days) + " days old"
