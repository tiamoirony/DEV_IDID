# Generated by Django 4.1.4 on 2023-01-19 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contents", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="content", options={"ordering": ["-created_at"]},
        ),
    ]
