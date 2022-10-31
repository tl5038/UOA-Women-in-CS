from django.contrib import admin

from base.admin import GenericImageInline

from .models import EventModel


@admin.register(EventModel)
class EventAdmin(admin.ModelAdmin):
    fields = ("title", "event_date", "event_date_end", "body", "registration_url", "external_url", "tags")
    inlines = [GenericImageInline]
    search_fields = ("title", "body")
    list_display = ("title", "event_date", "event_date_end")
