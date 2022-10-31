from django.contrib import admin
from django.contrib.admin import TabularInline
from django.db.models import Count

from .models import Resource, ResourceCategory


class CategoryInlineAdmin(TabularInline):
    extra = 1
    model = Resource


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInlineAdmin]
    search_fields = ("name",)
    list_display = ("name", "resource_count")

    @admin.display(description="Number of resources")
    def resource_count(self, obj):
        return obj.resource_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(resource_count=Count("resources"))
