from django.contrib import admin

from base.admin import GenericImageInline

from .models import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    fields = ("title", "subtitle", "body", "tags")
    inlines = [GenericImageInline]
    search_fields = ("title", "body")
    list_display = ("title", "created_at", "updated_at")
