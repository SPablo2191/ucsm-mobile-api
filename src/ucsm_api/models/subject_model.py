from django.contrib import admin
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.academic_program_model import AcademicProgram
from ucsm_api.models.semester_model import Semester

class Subject(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    name = models.CharField(max_length=150, blank=True, default="")
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    academic_program = models.ForeignKey(AcademicProgram, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id","name","semester","academic_program")