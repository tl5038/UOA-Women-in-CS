from django.contrib import admin
from django.contrib.admin import TabularInline

from base.admin import GenericImageInline

from .models import Project, ProjectParticipant, ProjectSupervisor


class BaseProjectPersonInline(TabularInline):
    extra = 0
    autocomplete_fields = ("profile",)


class ProjectSupervisorInline(BaseProjectPersonInline):
    model = ProjectSupervisor


class ProjectParticipantInline(BaseProjectPersonInline):
    model = ProjectParticipant


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [GenericImageInline, ProjectSupervisorInline, ProjectParticipantInline]
    search_fields = ("name", "description")
    list_display = ("name", "created_at", "updated_at")
