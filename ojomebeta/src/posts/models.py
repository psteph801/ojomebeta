from django.db import models

# Create your models here.


class post(models.Model):

	description 	= models.TextField()
	description1 	= models.TextField()
	description2 	= models.TextField()
	timestamp		= models.DateTimeField(auto_now=True)
	updated			= models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.posttitle)

		