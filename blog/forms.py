from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ["post"]
		labels = {
			"user_name": "Your Name",
			"e_mail": "Your E-Mail",
			"text": "Your Comment"
		}