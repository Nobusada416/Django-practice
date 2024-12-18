# Generated by Django 5.1.2 on 2024-11-07 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ModelApp", "0004_authors_books"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="prefecture",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="ModelApp.prefectures",
            ),
            preserve_default=False,
        ),
    ]
