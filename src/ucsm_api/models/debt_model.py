from django.contrib import admin
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.enrollment_model import Enrollment

class Debt(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    balance = models.DecimalField(max_digits=10,decimal_places=2) # recommend for money purpose
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    updated_date = models.DateTimeField(default=timezone.now)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.balance} - {self.enrollment}"

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ("id","balance","enrollment","status")