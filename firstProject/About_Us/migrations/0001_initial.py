# Generated by Django 4.2.5 on 2023-09-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="teacher",
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
                ("tid", models.IntegerField()),
                ("tname", models.CharField(max_length=40)),
                ("temail", models.EmailField(max_length=30)),
            ],
        ),
    ]
