from django.contrib import admin
from polymorphic.admin import PolymorphicChildModelAdmin, PolymorphicChildModelFilter, PolymorphicParentModelAdmin

from .models import BaseProfileModel, PhDStudentProfileModel, StaffProfileModel


class ProfileChildModelAdmin(PolymorphicChildModelAdmin):
    base_model = BaseProfileModel
    search_fields = ["name"]
    list_display = ["name", "updated_at", "email", "external_url"]


@admin.register(BaseProfileModel)
class ProfileParentModelAdmin(PolymorphicParentModelAdmin):
    base_model = BaseProfileModel
    child_models = [StaffProfileModel, PhDStudentProfileModel]
    list_filter = (PolymorphicChildModelFilter,)
    search_fields = ["name"]

    # Hide the parent model from admin
    def has_module_permission(self, request):
        return False


@admin.register(StaffProfileModel)
class StaffModelAdmin(ProfileChildModelAdmin):
    base_model = StaffProfileModel
    show_in_index = True


@admin.register(PhDStudentProfileModel)
class PhDStudentModelAdmin(ProfileChildModelAdmin):
    base_model = PhDStudentProfileModel
    show_in_index = True
