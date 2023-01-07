# Generated by Django 4.1.4 on 2023-01-03 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "code",
                    models.CharField(
                        max_length=4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="도서코드",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="도서명")),
                ("author", models.CharField(max_length=50, verbose_name="저자")),
                ("price", models.IntegerField(verbose_name="도서정가")),
                (
                    "register_dttm",
                    models.DateTimeField(auto_now_add=True, verbose_name="등록날짜"),
                ),
            ],
            options={"db_table": "bookbl",},
        ),
    ]