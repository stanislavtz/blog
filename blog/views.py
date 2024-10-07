from django.views.generic import ListView, DetailView

from .models import Post, Author

# Create your views here.

class HomePageView(ListView):
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    template_name = "blog/index.html"

    def get_queryset(self):
        query = super().get_queryset()[:3]
        return query


class AllPostsView(ListView):
    model = Post
    ordering = ["date"]
    context_object_name = "posts"
    template_name = "blog/all-posts.html"


class PostDetailsView(DetailView):
    model = Post
    template_name = "blog/post-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["tags"] = self.object.tags.all()
        return context


class AuthorDetailsView(DetailView):
    model = Author
    template_name = "blog/author-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["posts"] = self.object.posts.all()
        return context
