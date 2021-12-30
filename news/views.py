from django.shortcuts import render

# Create your views here.

from news.models import NewsModels


def news(request, pk):
    if request.method == "GET":
        type_news = NewsModels.objects.filter(article_type_id=pk, status=True)
        return render(request, 'news.html', locals())


def arts(request, pk):
    new = NewsModels.objects.filter(pk=pk, status=True).first()
    return render(request, 'art.html', locals())
