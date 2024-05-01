from django.contrib import admin
from django.db import models
import uuid

class Building(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=150, blank=True, default="")
    def __str__(self):
        return self.name

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("id","name")