# Generated by Django 4.2.5 on 2023-09-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aiquest",
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
                ("teacher_name", models.CharField(max_length=25)),
                ("course_name", models.CharField(max_length=25)),
                ("course_duration", models.IntegerField()),
                ("seat", models.IntegerField()),
            ],
        ),
    ]