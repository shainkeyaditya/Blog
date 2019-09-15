from django.db import models

# Create your models here.
from django.db.models import TextField


# first add the blog-article


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Author")
    content = TextField()
    title = models.CharField(max_length=50, verbose_name="Title")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    article_image = models.FileField(blank=True, null=True, verbose_name="Add Photo to Article")

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Article", related_name="comments")
    comment_content = models.CharField(max_length=200, verbose_name="comment")
    comment_user = models.CharField(max_length=50, verbose_name="Name")
    comment_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(verbose_name='Notes')

    def __str__(self):
        return self.comment_content
