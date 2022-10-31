import datetime

from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import EventModel


class TestEvents(TestCase):
    def test_constraint(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                EventModel.objects.create(
                    title="Test Event",
                    event_date=timezone.now(),
                    event_date_end=timezone.now() - datetime.timedelta(days=1),
                )
        now = timezone.now()
        EventModel.objects.create(title="Test Event", event_date=now, event_date_end=now + datetime.timedelta(days=1))
        EventModel.objects.create(title="Test Event", event_date=now, event_date_end=now)

    def test_unique_slug(self):
        now = timezone.now()
        EventModel.objects.create(title="Test Event", event_date=now, event_date_end=now + datetime.timedelta(days=1))
        EventModel.objects.create(title="Test Event", event_date=now, event_date_end=now + datetime.timedelta(days=1))
        self.assertEqual(EventModel.objects.count(), 2)
        self.assertEqual(EventModel.objects.get(slug="test-event").title, "Test Event")
        self.assertEqual(EventModel.objects.get(slug="test-event-2").title, "Test Event")

    def test_event_not_exist(self):
        response = self.client.get(reverse("event-single", kwargs={"slug": "does-not-exist"}))
        self.assertEqual(response.status_code, 404)
