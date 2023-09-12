from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)
	mode_of_transportation = models.CharField(max_length=20)
	sem1_backlogs = models.CharField(max_length=20)
	sem2_backlogs = models.CharField(max_length=20)
	sem3_backlogs = models.CharField(max_length=20)
	sem4_backlogs = models.CharField(max_length=20)
	sem5_backlogs = models.CharField(max_length=20)
	sem6_backlogs = models.CharField(max_length=20)
	sem7_backlogs = models.CharField(max_length=20)
	sem8_backlogs = models.CharField(max_length=20)
	

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
