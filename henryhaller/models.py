from django.db import models

# Create your models here.

class BlogPost(models.Model):
	pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length=500)
	text = models.TextField()
	def __unicode__(self): return self.title
	def pretty_age(self):
		pass
