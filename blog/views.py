from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "blog/index.html")


def all_posts(request):
	pass


def post_details(request, slug):
	pass