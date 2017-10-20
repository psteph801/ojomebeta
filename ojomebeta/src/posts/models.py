from django.conf import settings
from django.db import models

# Create your models here.


class post(models.Model):
	user			= models.ForeignKey(settings.AUTH_USER_MODEL)
	description 	= models.TextField(max_length=280)
	description1 	= models.TextField(max_length=280)
	description2 	= models.TextField(max_length=280)
	timestamp		= models.DateTimeField(auto_now=True)
	updated			= models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return str(self.description)

		