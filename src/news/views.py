from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import NewsModel


def news_list(request):
    object_split = 5
    news_list = NewsModel.objects.all().order_by("-created_at")
    if len(news_list):
        latest_news = news_list[0]
    else:
        latest_news = 0
    paginator = Paginator(news_list, object_split)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = paginator.page_range
    return render(
        request, "news/news_list.html", {"objects": page_obj, "page_range": page_range, "latest_news": latest_news}
    )


def news_full(request, slug):
    news = NewsModel.objects.filter(slug=slug).first()
    if not news:
        return HttpResponseNotFound()
    return render(request, "news/news_full.html", {"news": news})


def list_by_tag(request, tag_slug):
    object_split = 5
    news_list = NewsModel.objects.filter(tags__slug=tag_slug).order_by("-created_at")
    if len(news_list) == 0:
        return HttpResponseNotFound()
    if len(news_list):
        latest_news = news_list[0]
    else:
        latest_news = 0
    paginator = Paginator(news_list, object_split)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = paginator.page_range
    return render(
        request,
        "news/news_list.html",
        {"objects": page_obj, "page_range": page_range, "latest_news": latest_news, "tag": tag_slug},
    )
