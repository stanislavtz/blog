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
        form = CommentForm()
        context = self.get_context(request, post, form)

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

        context = self.get_context(request, post, form)

        return render(request, self.template_name, context)

    @staticmethod
    def get_context(request, post, form):
        add_for_later_list = request.session.get("read_later_posts")
        if not add_for_later_list:
            add_for_later_list = []

        return {
            "post": post,
            "tags": post.tags.all(),
            "post_comments": post.comments.all().order_by("-id"),
            "comment_form": form,
            "add_for_later": post.id in add_for_later_list
        }


class ReadLaterView(View):
    @staticmethod
    def post(request):
        stored_posts = request.session.get("read_later_posts")

        if not stored_posts: # if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["read_later_posts"] = stored_posts

        print(stored_posts)

        return HttpResponseRedirect("/")


class AuthorDetailsView(DetailView):
    model = Author
    template_name = "blog/author-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["posts"] = self.object.posts.all()
        return context
