# Generated by Django 5.1.2 on 2024-11-02 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ModelApp", "0001_add_person"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prefectures",
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
                ("name", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "prefectures",
            },
        ),
        migrations.CreateModel(
            name="Schools",
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
                ("name", models.CharField(max_length=20)),
                (
                    "prefecture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ModelApp.prefectures",
                    ),
                ),
            ],
            options={
                "db_table": "schools",
            },
        ),
        migrations.CreateModel(
            name="Students",
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
                ("name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("major", models.CharField(max_length=20)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="ModelApp.schools",
                    ),
                ),
            ],
            options={
                "db_table": "students",
            },
        ),
    ]
