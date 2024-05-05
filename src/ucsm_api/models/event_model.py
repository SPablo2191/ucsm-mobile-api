from django.contrib import admin
from django.db import models
from django.utils import timezone
from datetime import date
import uuid

from ucsm_api.models.building_model import Building
from ucsm_api.models.utils import TableStatus

class Event(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField(default="",blank=True)
    image_url =  models.CharField(max_length=200, blank=True, default="")
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id","name","description")
