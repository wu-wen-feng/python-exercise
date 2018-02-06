from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def test(request):
    return HttpResponse("This is test")


def index(request):
    # article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request, 'myapp/index.html', {"articles": articles})


def detail(request, id):
    article = models.Article.objects.get(pk=id)
    return render(request, 'myapp/detail.html', {"article": article})


def edit(request, id):
    if str(id) == "0":
        return render(request, 'myapp/edit.html')
    else:
        article = models.Article.objects.get(pk=id)
        return render(request, 'myapp/edit.html', {"article": article})


def save(request):
    id = request.POST.get("id", "0")
    title = request.POST.get("title", "title_default")
    content = request.POST.get("content", "content_default")
    if id == '0':
        models.Article.objects.create(title=title, content=content)
        # articles = models.Article.objects.all()
        # return render(request, 'myapp/index.html', {"articles": articles})
    else:
        article = models.Article.objects.get(pk=id)
        article.title = title
        article.content = content
        article.save()
        # return render(request, 'myapp/detail.html', {"article": article})
    articles = models.Article.objects.all()
    return render(request, 'myapp/index.html', {"articles": articles})
