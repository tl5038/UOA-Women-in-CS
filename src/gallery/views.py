from django.shortcuts import render
from django.core.paginator import Paginator

from .models import GalleryModel


def gallery_list(request):
    return render(request, "gallery/gallery_list.html", {"galleries": GalleryModel.objects.all()})


def gallery_page(request, slug):
    gallery = GalleryModel.objects.get(slug=slug)
    images = gallery.images.all()
    paginator = Paginator(images, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"gallery": gallery, "images": images, "page_obj": page_obj}

    return render(request, "gallery/gallery_page.html", context)
