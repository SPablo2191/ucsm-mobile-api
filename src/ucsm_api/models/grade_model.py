from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

import uuid
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.student_commission_model import StudentCommission

class Phase(models.TextChoices):
    FIRST = "PRIMERA FASE"
    SECOND = "SEGUNDA FASE"
    THIRD = "TERCERA FASE"


class Grade(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    student_commision = models.ForeignKey(StudentCommission,on_delete=models.CASCADE)
    score = models.IntegerField(
        blank=True, default=0, validators=[MaxValueValidator(20), MinValueValidator(0)]
    )
    phase = models.CharField(max_length=20, default=Phase.FIRST, choices=Phase.choices)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.student_commision}: {self.phase}-{self.score}"


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("id", "student_commision", "score", "phase")
