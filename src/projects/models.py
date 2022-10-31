from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Q

from base.models import Image
from profiles.models import BaseProfileModel


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    external_url = models.URLField(blank=True, help_text="Optional")
    images = GenericRelation(Image)
    slug = AutoSlugField(populate_from="name", unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_model_name(self):
        return self._meta.model_name


def PERSON_PROFILE_SET_NULL_SAFE(collector, field, sub_objs, using):
    """
    Equivalent to SET_NULL but specific for ProjectPerson.

    Due to the constraint on ProjectPerson that we have to have a name or profile,
    we can't delete a profile if it is linked to a ProjectPerson.

    To work around this we set the ProjectPerson name to the profile name before deletion.
    """
    person = sub_objs.first()
    if not person.name:
        collector.add_field_update(sub_objs.first()._meta.get_field("name"), person.profile.name, sub_objs)
    models.SET_NULL(collector, field, sub_objs, using)


class ProjectPerson(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="%(class)s")
    profile = models.ForeignKey(
        BaseProfileModel,
        on_delete=PERSON_PROFILE_SET_NULL_SAFE,
        null=True,
        blank=True,
        help_text="Optional profile to link to for this person",
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        help_text="Name for this person if they do not have a profile.",
        verbose_name="Name override",
    )

    class Meta:
        abstract = True

        # Ensure that there is either a name or profile linked to this person
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_name_or_profile",
                check=(
                    Q(Q(profile__isnull=True) & ~Q(name__exact=""))
                    | Q(Q(profile__isnull=False) & Q(name__exact=""))
                    | Q(Q(profile__isnull=False) & ~Q(name__exact=""))
                ),
                violation_error_message="A profile and/or name must be provided",
            )
        ]

    def __str__(self):
        return self.name or self.profile.name if self.profile else super().__str__()


class ProjectSupervisor(ProjectPerson):
    class Meta(ProjectPerson.Meta):
        verbose_name = "Supervisor"


class ProjectParticipant(ProjectPerson):
    class Meta(ProjectPerson.Meta):
        verbose_name = "Participant"
