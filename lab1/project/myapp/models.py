from django.db import models

# Create your models here.
class Register(models.Model):
	fname=models.CharField(max_length=30)
	lname=models.CharField(max_length=30)
	email=models.EmailField()
	Pas=models.CharField(max_length=30)
	cpas=models.CharField(max_length=30)


	def __str__(self):
		return self.fname+" "+self.lname