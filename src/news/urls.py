from django.urls import path

from . import views

urlpatterns = [
    path("", views.news_list, name="news-list"),
    path("<slug>", views.news_full, name="news-single"),
    path("tag/<slug:tag_slug>", views.list_by_tag, name="news-list-by-tag"),
]
