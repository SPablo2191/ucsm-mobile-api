# Generated by Django 4.2.11 on 2024-05-07 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ucsm_api", "0017_studentcommission"),
    ]

    operations = [
        migrations.AddField(
            model_name="commission",
            name="commission_type",
            field=models.CharField(default="Teoría", max_length=20),
        ),
    ]
