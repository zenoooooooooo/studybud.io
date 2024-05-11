# Generated by Django 5.0.4 on 2024-05-04 03:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_delete_gawgkawk"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ["-updated", "-created"]},
        ),
        migrations.AddField(
            model_name="room",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
