# Generated by Django 4.1.4 on 2022-12-29 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo", old_name="complate", new_name="complete",
        ),
    ]
