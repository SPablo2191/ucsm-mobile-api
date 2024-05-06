from django.contrib import admin
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.utils import TableStatus

class Day(models.TextChoices):
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'

class CommissionSchedule(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    day = models.CharField(max_length=20, default=Day.MONDAY,choices=Day.choices)
    start_time = models.TimeField() 
    end_time = models.TimeField() 
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.day}: {self.start_time}-{self.end_time}"

@admin.register(CommissionSchedule)
class CommissionScheduleAdmin(admin.ModelAdmin):
    list_display = ("id","day", "start_time","end_time")