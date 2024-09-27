from datetime import date

from django.http import Http404
from django.shortcuts import render

from .models import Post

posts = []


# Create your views here.

def index(request):
    try:
        latest_posts = Post.objects.all().order_by("-date")[:3]

        return render(request, "blog/index.html", {
            "posts": latest_posts,
            "has_posts": len(posts) > 0
        })
    except:
        raise Http404()


def get_all_posts(request):
    try:
        all_posts = Post.objects.all()
        return render(request, "blog/all-posts.html", { "posts": all_posts })
    except:
        raise Http404()


def post_details(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        return render(request, "blog/post-details.html", { "post": post })
    except:
        raise Http404()