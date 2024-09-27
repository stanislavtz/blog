from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	e_mail = models.EmailField(max_length=250)


class Post(models.Model):
	slug = models.CharField(max_length=100)
	image = models.ImageField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
	date = models.DateField()
	title = models.CharField(max_length=100)
	excerpt = models.TextField()
	content = models.TextField()

