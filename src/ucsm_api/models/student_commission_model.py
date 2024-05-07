from django.contrib import admin
from django.db import models
from django.utils import timezone
import uuid
from ucsm_api.models.subject_registration_model import SubjectRegistration
from ucsm_api.models.commission_model import Commission
from ucsm_api.models.utils import TableStatus

class StudentCommission(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    commission = models.ForeignKey(Commission,on_delete=models.CASCADE)
    subject_registration = models.ForeignKey(SubjectRegistration,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default=TableStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.commission} - {self.subject_registration}"
    
@admin.register(StudentCommission)
class StudentCommissionAdmin(admin.ModelAdmin):
    list_display = ("id","commission","subject_registration")