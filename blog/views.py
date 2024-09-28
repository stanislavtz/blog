from django.http import Http404
from django.shortcuts import render

from .models import Post, Author

# Create your views here.

def index(request):
    try:
        latest_posts = Post.objects.all().order_by("-date", "-id")[:3]

        return render(request, "blog/index.html", {
            "posts": latest_posts,
            "has_posts": len(latest_posts) > 0
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
        post = Post.objects.get(slug=slug)
        return render(request, "blog/post-details.html", {
            "post": post,
            "tags": post.tags.all()
        })
    except:
        raise Http404()


def get_author_details(request, id):
    author = Author.objects.get(id=id)
    author_posts = author.posts.all()

    return render(request, "blog/author-details.html", {
        "author": author,
        "posts": author_posts,
    })