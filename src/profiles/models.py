from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel


class BaseProfileModel(PolymorphicModel):
    """
    Using PolymorphicModel allows us to reference
    the base profile model of staff/phd in projects
    without having to reference the specific model
    """

    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    biography = RichTextField(null=True, blank=True)
    image = models.ImageField()
    external_url = models.URLField(blank=True, null=True)
    slug = AutoSlugField(populate_from="name", unique=True, unique_with="polymorphic_ctype_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"

    def __str__(self):
        return self.name

    def get_model_name(self):
        return self._meta.model_name


class StaffProfileModel(BaseProfileModel):
    class Meta:
        verbose_name = "Staff Profile"

    def get_absolute_url(self):
        return reverse("staff-single", kwargs={"slug": self.slug})


class PhDStudentProfileModel(BaseProfileModel):
    class Meta:
        verbose_name = "PhD Student Profile"

    def get_absolute_url(self):
        return reverse("phd-single", kwargs={"slug": self.slug})
