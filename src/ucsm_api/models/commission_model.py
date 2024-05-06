from django.contrib import admin
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.classroom_model import Classroom
from ucsm_api.models.commission_schedule_model import CommissionSchedule
from ucsm_api.models.professor_model import Professor

class Commission(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    commission_schedule = models.OneToOneField(CommissionSchedule, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.professor} - {self.classroom} - {self.commission_schedule}"

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ("id","professor","classroom","commission_schedule")