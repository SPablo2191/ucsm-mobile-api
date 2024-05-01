from django.db import models
from django.contrib import admin
from django.utils import timezone

import uuid
from .utils import TableStatus

class Professor(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    first_name = models.CharField(max_length=150, blank=True, default="")
    middle_name = models.CharField(max_length=150, blank=True, default="")
    last_name = models.CharField(max_length=150, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    identification_document = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
@admin.register(Professor)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("identification_document", "first_name", "last_name", "email")