from django.db import models
# Create your models here.

class DataModel(models.Model):
	naziv = models.CharField(max_length = 50)
	datoteka = models.FileField(upload_to='documents/%Y/%m/%d')

	def __str__(self):
		return self.naziv