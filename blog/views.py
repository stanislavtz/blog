from django.http import Http404
from django.shortcuts import render

from django.views.generic import ListView

from .models import Post, Author

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["has_posts"] = len(self.object_list) > 0
        print(self.object_list)
        return context

    def get_queryset(self):
        query = super().get_queryset().order_by("-date")[:3]
        return query


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