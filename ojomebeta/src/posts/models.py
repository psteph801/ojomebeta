from django.db import models

# Create your models here.


class post(models.Model):
	posttitle		 = models.TextField()
	description 	= models.TextField()
	description1 	= models.TextField()
	description2 	= models.TextField()
	def __str__(self):
		return str(self.posttitle)

		