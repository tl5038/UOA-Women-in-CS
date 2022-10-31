from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from base.models import Image


class GalleryModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    gallery_date = models.DateField(blank=True, null=True, help_text="Date of the gallery. Optional.")
    images = GenericRelation(Image)

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gallery-page", kwargs={"slug": self.slug})
