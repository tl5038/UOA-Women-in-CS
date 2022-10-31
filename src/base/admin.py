from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from taggit.admin import Tag

from .models import Image


class GenericImageInline(GenericTabularInline):
    model = Image
    extra = 0


admin.site.unregister(Tag)
