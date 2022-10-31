from django.db import models
from django.urls import reverse

from base.models import Article


class NewsModel(Article):
    subtitle = models.CharField(max_length=255, default=None)

    class Meta(Article.Meta):
        verbose_name = "News"
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return reverse("news-single", kwargs={"slug": self.slug})
