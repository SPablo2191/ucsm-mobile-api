from django.contrib import admin
from django.db import models
from datetime import date
from django.utils import timezone
import uuid
from .utils import TableStatus

class Semester(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=150, blank=True, default="")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("id","name", "start_date", "end_date")