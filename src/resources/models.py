from django.db import models

from base.models import ExternalResource


class ResourceCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Resource Category"
        verbose_name_plural = "Resource Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Resource(ExternalResource):
    category = models.ForeignKey(ResourceCategory, on_delete=models.CASCADE, related_name="resources")

    class Meta:
        ordering = ["category", "display_title"]
