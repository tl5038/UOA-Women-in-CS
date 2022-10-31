from django.db import IntegrityError, transaction
from django.test import TestCase

from profiles.models import StaffProfileModel

from .models import Project, ProjectParticipant, ProjectSupervisor


class ProjectTest(TestCase):
    def setUp(self):
        Project.objects.create(
            name="Test Project",
            description="Test Project Description",
        )

    def test_constraint(self):
        for m in (ProjectSupervisor, ProjectParticipant):
            with self.assertRaises(IntegrityError):
                with transaction.atomic():
                    m.objects.create(project=Project.objects.get(name="Test Project"))

            m.objects.create(project=Project.objects.get(name="Test Project"), name="Test Supervisor")
            m.objects.create(
                project=Project.objects.get(name="Test Project"),
                name="Test Supervisor",
                profile=StaffProfileModel.objects.create(name="Test Supervisor"),
            )
            m.objects.create(
                project=Project.objects.get(name="Test Project"),
                profile=StaffProfileModel.objects.create(name="Test Supervisor"),
            )

    def test_delete_profile_set_all(self):
        for person in (ProjectSupervisor, ProjectParticipant):
            profile = StaffProfileModel.objects.create(name="Staff Test")
            person_obj = person.objects.create(
                project=Project.objects.get(name="Test Project"),
                profile=profile,
            )

            profile.delete()
            person_obj.refresh_from_db()
            self.assertEqual(person_obj.profile, None)
            self.assertEqual(person_obj.name, "Staff Test")

    def test_delete_profile_dont_set(self):
        for person in (ProjectSupervisor, ProjectParticipant):
            profile = StaffProfileModel.objects.create(name="Staff Test")
            person_obj = person.objects.create(
                project=Project.objects.get(name="Test Project"),
                profile=profile,
                name="Override Staff",
            )

            profile.delete()
            person_obj.refresh_from_db()
            self.assertEqual(person_obj.profile, None)
            self.assertEqual(person_obj.name, "Override Staff")

    def test_unique_slug(self):
        Project.objects.create(name="A Test Project")
        Project.objects.create(name="A Test Project")
        self.assertEqual(Project.objects.count(), 3)
        self.assertEqual(Project.objects.get(slug="a-test-project").name, "A Test Project")
        self.assertEqual(Project.objects.get(slug="a-test-project-2").name, "A Test Project")
