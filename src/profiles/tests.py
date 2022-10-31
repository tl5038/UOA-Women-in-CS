from django.test import TestCase
from django.urls import reverse

from .models import PhDStudentProfileModel, StaffProfileModel


class TestProfile(TestCase):
    def test_unique_slug(self):
        for model in (PhDStudentProfileModel, StaffProfileModel):
            model.objects.create(name="Test 1")
            model.objects.create(name="Test 1")
            self.assertEqual(model.objects.count(), 2)
            self.assertEqual(model.objects.get(slug="test-1").name, "Test 1")
            self.assertEqual(model.objects.get(slug="test-1-2").name, "Test 1")

    def test_phd_not_exist(self):
        response = self.client.get(reverse("phd-single", kwargs={"slug": "does-not-exist"}))
        self.assertEqual(response.status_code, 404)

    def test_staff_not_exist(self):
        response = self.client.get(reverse("staff-single", kwargs={"slug": "does-not-exist"}))
        self.assertEqual(response.status_code, 404)
