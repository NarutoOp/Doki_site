from django.db import models
from django.utils import timezone

class project(models.Model):
	title = models.CharField(max_length=100)
	# date_posted = models.DateTimeField(default=timezone.now)
	date_posted = models.CharField(max_length=100)
	class Meta:
		db_table = "project"

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('post-detail',kwargs = {'pk' : self.pk })