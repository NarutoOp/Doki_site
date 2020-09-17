from django.db import models
from django.utils import timezone

class project(models.Model):
	title = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	project_img = models.ImageField(default='images/item-3.png',upload_to='images/')
	content = models.TextField(default="Hello")


	def __str__(self):
		return self.title

	def delete(self,*args,**kwargs):
		self.project_img.delete()
		super().delete(*args,**kwargs)

class post(models.Model):
	title = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	post_img = models.ImageField(default='images/item-3.png',upload_to='images/')
	content = models.TextField(default="Hello")


	def __str__(self):
		return self.title

	def delete(self,*args,**kwargs):
		self.post_img.delete()
		super().delete(*args,**kwargs)