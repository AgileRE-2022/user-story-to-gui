from django.db import models

class UserStory(models.Model):
	role = models.CharField(max_length=50)
	task = models.CharField(max_length=250)
	benefit = models.CharField(max_length=250)
	initState = models.CharField(max_length=500)
	action = models.CharField(max_length=500)
	result = models.CharField(max_length=500)
	
	#menamakan objek dalam db (biar ga objek 1, objek 2)
	def __str__(self):
		return self.user
