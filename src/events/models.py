from datetime import timedelta

from django.db import models
from django.db.models import Q
from django.urls import reverse

from base.models import Article


class EventModel(Article):
    event_date = models.DateTimeField(verbose_name="Event date and time")
    event_date_end = models.DateTimeField(
        verbose_name="Event end date and time", blank=True, null=True, help_text="Defaults to 1 hour after start time"
    )
    registration_url = models.URLField(blank=True, null=True, help_text="URL to register for the event. Optional.")
    external_url = models.URLField(
        blank=True, null=True, help_text="URL to an external page for further event information. Optional."
    )

    def save(self, *args, **kwargs):
        if not self.event_date_end and self.event_date:
            self.event_date_end = self.event_date + timedelta(hours=1)
            self.save()
        super().save(*args, **kwargs)

    class Meta(Article.Meta):
        verbose_name = "Event"
        verbose_name_plural = "Events"
        constraints = [
            models.CheckConstraint(
                check=(Q(event_date_end__isnull=True) | Q(event_date_end__gte=models.F("event_date"))),
                name="end_date must be greater than or equal to start_date",
                violation_error_message="Event end date must be greater than or equal to the event start date.",
            )
        ]

    def get_absolute_url(self):
        return reverse("event-single", kwargs={"slug": self.slug})
