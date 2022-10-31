from django.urls import path  # noqa: F401
from . import views  # noqa: F401

urlpatterns = [
    path("", views.gallery_list, name="gallery-list"),
    path("<slug:slug>", views.gallery_page, name="gallery-page"),
]
