from django.db import models

# Create your models here.
class prodmodel(models.Model):
	PName=models.CharField(max_length=30)
	PBrand=models.CharField(max_length=30)
	PPrice=models.IntegerField(default=50)
	Stock=models.CharField(max_length=30)