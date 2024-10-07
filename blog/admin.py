from django.contrib import admin
from .models import Post, Author, Tag, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {
		"slug": ("title",)
	}

	list_display = ("title", "id", "date", "author")
	list_filter = ("title", "author", "date", "tags")


class CommentAdmin(admin.ModelAdmin):
	list_display = ("user_name", "e_mail", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
