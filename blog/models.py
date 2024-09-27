from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	e_mail = models.EmailField(max_length=250)




