from django.contrib import admin
from django.db import models
from django.utils import timezone
from datetime import date
import uuid

from ucsm_api.models.building_model import Building
from ucsm_api.models.utils import TableStatus

class Classroom(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=100, blank=True, default="")
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        aux = self.building.__str__().split(" ")
        if aux[0].lower() == "pabellón":
            classroom = aux[1]+"-"+self.name
        else:
            classroom = self.name
        return classroom

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ("id","name","building")
