from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index-page"),
	path("posts", views.all_posts, name="all-posts-page"),
	path("<slug>/post_details", views.post_details, name="post-details-page")
]