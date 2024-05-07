# Generated by Django 4.2.11 on 2024-05-07 01:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("ucsm_api", "0016_subjectregistration"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentCommission",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("status", models.CharField(default="ACTIVE", max_length=20)),
                (
                    "register_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "commission",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ucsm_api.commission",
                    ),
                ),
                (
                    "subject_registration",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ucsm_api.subjectregistration",
                    ),
                ),
            ],
        ),
    ]
