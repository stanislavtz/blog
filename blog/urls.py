from django.urls import path
from . import views

urlpatterns = [
	path("", views.HomePageView.as_view(), name="index-page"),
	path("posts", views.get_all_posts, name="all-posts-page"),
	path("posts/<slug:slug>", views.post_details, name="post-details-page"),
	path("author/<id>", views.get_author_details, name="author-details-page")
]