from django.contrib import admin
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.academic_program_model import AcademicProgram
from ucsm_api.models.student_model import Student

class Enrollment(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    academic_program = models.ForeignKey(AcademicProgram, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student_code = models.CharField(max_length=150, blank=True, default="")
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student_code} - {self.student}"

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("id","student_code","student","academic_program")