from django.db import models

# Create your models here.
class Userimages(models.Model):
	fullname=models.CharField(max_length=100)
	mailid=models.EmailField()
	image=models.FileField(upload_to='profilepics/')


	def __str__(self):
		return self.fullname