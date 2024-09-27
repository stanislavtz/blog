from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index-page"),
	path("posts", views.get_all_posts, name="all-posts-page"),
	path("posts/<slug:slug>", views.post_details, name="post-details-page")
]