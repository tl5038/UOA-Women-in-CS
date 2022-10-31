from django.contrib import admin
from django.db.models import Count

from .models import GalleryModel
from base.admin import GenericImageInline


@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    fields = ("title", "gallery_date")
    search_fields = ("title", "gallery_date")
    list_display = ("title", "gallery_date", "image_count")
    inlines = [GenericImageInline]

    @admin.display(description="Number of images")
    def image_count(self, obj):
        return obj.image_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(image_count=Count("images"))
