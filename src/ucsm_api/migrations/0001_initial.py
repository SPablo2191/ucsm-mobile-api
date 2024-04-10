# Generated by Django 4.2.11 on 2024-04-10 20:31

import datetime
from django.db import migrations, models
import django.utils.timezone
import ucsm_api.models.student_model
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
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
                (
                    "first_name",
                    models.CharField(blank=True, default="", max_length=150),
                ),
                (
                    "middle_name",
                    models.CharField(blank=True, default="", max_length=150),
                ),
                ("last_name", models.CharField(blank=True, default="", max_length=150)),
                (
                    "second_last_name",
                    models.CharField(blank=True, default="", max_length=150),
                ),
                ("email", models.EmailField(blank=True, default="", max_length=254)),
                ("birth_date", models.DateField(default=datetime.date.today)),
                (
                    "phone_number",
                    models.CharField(blank=True, default="", max_length=20),
                ),
                ("address", models.TextField(blank=True, default="")),
                (
                    "identification_document",
                    models.CharField(max_length=50, unique=True),
                ),
                ("status", models.CharField(default="ACTIVE", max_length=20)),
                (
                    "register_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student",
                "verbose_name_plural": "Students",
            },
            managers=[
                ("objects", ucsm_api.models.student_model.StudentManager()),
            ],
        ),
    ]
