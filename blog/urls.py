from django.urls import path
from . import views

urlpatterns = [
	path("", views.index),
	path("posts", views.all_posts),
	path("<slug>/post_details", views.post_details)
]