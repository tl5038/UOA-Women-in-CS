from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Project


def project(request):
    object_split = 5
    projects = Project.objects.all().order_by("-created_at")
    paginator = Paginator(projects, object_split)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = paginator.page_range
    return render(request, "projects/projects.html", {"objects": page_obj, "page_range": page_range})
