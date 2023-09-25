# Generated by Django 4.2.5 on 2023-09-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("image", models.CharField(max_length=100)),
                ("title_of_work", models.CharField(max_length=100)),
                ("artist", models.CharField(max_length=100)),
                ("review", models.CharField(max_length=100)),
            ],
        ),
    ]