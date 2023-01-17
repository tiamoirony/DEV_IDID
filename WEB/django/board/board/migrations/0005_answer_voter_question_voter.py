# Generated by Django 4.1.4 on 2023-01-13 05:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("board", "0004_rename_answer_comment_answer"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_answer",
                to=settings.AUTH_USER_MODEL,
                verbose_name="추천수",
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_question",
                to=settings.AUTH_USER_MODEL,
                verbose_name="추천수",
            ),
        ),
    ]
