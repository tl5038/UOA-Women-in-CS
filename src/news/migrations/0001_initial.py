# Generated by Django 4.1.1 on 2022-10-23 09:14

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsModel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", autoslug.fields.AutoSlugField(editable=False, populate_from="title", unique=True)),
                ("title", models.CharField(max_length=255)),
                ("body", ckeditor.fields.RichTextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("subtitle", models.CharField(default=None, max_length=255)),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "News",
                "verbose_name_plural": "News",
                "ordering": ["-created_at"],
                "abstract": False,
            },
        ),
    ]
