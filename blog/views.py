from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "blog/index.html")


def all_posts(request):
	return render(request, "blog/all-posts.html")


def post_details(request, slug):
	pass