from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Author(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	e_mail = models.EmailField(max_length=250)


class Post(models.Model):
	title = models.CharField(max_length=150)
	excerpt = models.CharField(max_length=200)
	image_name = models.CharField(max_length=100)
	date = models.DateField(auto_now=True)
	slug = models.SlugField(unique=True)
	content = models.TextField(validators=[MinLengthValidator(10)])
	author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts")


class Tag(models.Model):
	caption = models.CharField(50)

