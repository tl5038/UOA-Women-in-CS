from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from taggit.managers import TaggableManager


class Image(models.Model):
    image = models.ImageField()
    short_description = models.CharField(blank=True, null=True, max_length=255)
    content_object = GenericForeignKey("content_type", "object_id")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Article(models.Model):
    slug = AutoSlugField(populate_from="title", unique=True)
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = GenericRelation(Image)
    tags = TaggableManager(blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self._meta.model_name


class ExternalResource(models.Model):
    url = models.URLField()
    display_title = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.display_title
