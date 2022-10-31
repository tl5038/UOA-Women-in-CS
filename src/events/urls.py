from django.urls import path

from . import views

urlpatterns = [
    path("", views.event_list, name="event-list"),
    path("<slug>", views.event_full, name="event-single"),
    path("tag/<slug:tag_slug>", views.list_by_tag, name="event-list-by-tag"),
]
