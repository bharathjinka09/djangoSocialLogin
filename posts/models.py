from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('home')