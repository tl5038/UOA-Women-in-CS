import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import EventModel
from news.models import NewsModel
from profiles.models import PhDStudentProfileModel, StaffProfileModel
from projects.models import Project

from .views import SelectorEnum


class TestSearch(TestCase):
    def setUp(self):
        StaffProfileModel.objects.create(name="Test Staff")
        PhDStudentProfileModel.objects.create(name="Test PhD")
        EventModel.objects.create(
            title="Test Event", event_date=timezone.now(), event_date_end=timezone.now() + datetime.timedelta(days=1)
        )
        NewsModel.objects.create(title="Test News", subtitle="Test News", body="Test News")
        Project.objects.create(
            name="Test Project",
            description="Test Project Description",
        )

    def test_empty_search(self):
        for selected in SelectorEnum:
            response = self.client.get(reverse("search"), {"selected": selected.value})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "search/search.html")
            self.assertIn(b"0 result has been found", response.content)
            response = self.client.get(reverse("search"), {"selected": selected.value, "searched": ""})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "search/search.html")
            self.assertIn(b"0 result has been found", response.content)

    def test_bad_selector(self):
        response = self.client.get(reverse("search"), {"selected": "bad_selector"})
        self.assertEqual(response.status_code, 400)
        response = self.client.get(reverse("search"))  # should default to "everything"
        self.assertEqual(response.status_code, 200)

    def test_bad_method(self):
        response = self.client.post(reverse("search"), {"selected": "Everything"})
        self.assertEqual(response.status_code, 405)
