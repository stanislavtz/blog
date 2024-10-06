from django.views.generic import ListView, DetailView

from .models import Post, Author

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["has_posts"] = len(self.object_list) > 0
        return context

    def get_queryset(self):
        query = super().get_queryset().order_by("-date")[:3]
        return query


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "posts"


class PostDetailsView(DetailView):
    model = Post
    template_name = "blog/post-details.html"


class AuthorDetailsView(DetailView):
    model = Author
    template_name = "blog/author-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["posts"] = self.object.posts.all()
        return context
