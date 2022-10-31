from django.shortcuts import render

from .models import ResourceCategory


def resources(request):
    categories = ResourceCategory.objects.all()
    return render(request, "resources/resources.html", {"categories": categories})
