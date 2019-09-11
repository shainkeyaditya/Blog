from django.db import models

# Create your models here.
# first add the blog-article
from sqlparse.tokens import Text


class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Author")
    content = Text()
    title = models.CharField(max_length=50, verbose_name="Title")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    article_image = models.FileField(blank=True, null=True, verbose_name="Add Photo to Article")