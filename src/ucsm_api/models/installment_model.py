from django.contrib import admin
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.debt_model import Debt


class Installment(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # recommend for money purpose
    paid_amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # recommend for money purpose
    owed_amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # recommend for money purpose
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=timezone.now)
    code = models.CharField(max_length=20, blank=True, default="00")
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    updated_date = models.DateTimeField(default=timezone.now)
    register_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.code} - {self.total_amount}"


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ("id", "total_amount", "code", "paid_amount", "owed_amount", "debt")
