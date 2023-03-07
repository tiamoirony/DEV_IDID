# Generated by Django 4.1.4 on 2023-01-19 05:19

import contents.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                ("text", models.TextField(default="")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                ("image", models.ImageField(upload_to=contents.models.image_upload_to)),
                ("order", models.SmallIntegerField()),
                (
                    "content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contents.content",
                        verbose_name="작성글",
                    ),
                ),
            ],
            options={"ordering": ["order"],},
        ),
        migrations.AddConstraint(
            model_name="image",
            constraint=models.UniqueConstraint(
                fields=("content", "order"), name="unique_together"
            ),
        ),
    ]