from django.http import request, HttpResponse
from django.shortcuts import render

# Create your views here.
from article.models import Article


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})


def index(request):
    return render(request, "index.html", {"name":"shainkey"})