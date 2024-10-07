from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post, Author, Comment
from .forms import CommentForm

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


class PostDetailsView(View):
    template_name = "blog/post-details.html"

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "tags": post.tags.all(),
            "post_comments": post.comments.all(),
            "comment_form": CommentForm()
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if form.is_valid():
            data = form.cleaned_data
            new_comment = Comment(
                user_name=data["user_name"],
                e_mail=data["e_mail"],
                text=data["text"],
                post=post
            )
            new_comment.save()
            return HttpResponseRedirect(reverse("post-details-page", args=[slug]))

        context = {
            "post": post,
            "tags": post.tags.all(),
            "post_comments": post.comments.all(),
            "comment_form": form
        }

        return render(request, self.template_name, context)


class AuthorDetailsView(DetailView):
    model = Author
    template_name = "blog/author-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["posts"] = self.object.posts.all()
        return context
