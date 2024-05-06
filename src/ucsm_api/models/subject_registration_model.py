from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.subject_model import Subject
from ucsm_api.models.enrollment_model import Enrollment


class SubjectRegistration(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    final_score = models.IntegerField(
        blank=True, default=0, validators=[MaxValueValidator(20), MinValueValidator(0)]
    )
    simulated_score = models.IntegerField(
        blank=True, default=0, validators=[MaxValueValidator(20), MinValueValidator(0)]
    )
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.enrollment} - {self.subject}"


@admin.register(SubjectRegistration)
class SubjectRegistrationAdmin(admin.ModelAdmin):
    list_display = ("id", "subject","enrollment","final_score","simulated_score")
