from django.contrib.auth.models import AbstractUser
from django.db import models
from enum import Enum
from datetime import date
class StudentStatus(Enum):
    """
    Use to filter per student status
    Return: 
    ACTIVE => It has an active enrollment
    INACTIVE => It doesnt have any active enrollment
    SUSPENDED => It is a block student
    """
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    SUSPENDED = 'SUSPENDED'

class Student(AbstractUser):
    middle_name = models.CharField(max_length=150, blank=True)
    second_last_name = models.CharField(max_length=150, blank=True)
    birth_date = models.DateField(default=date.today)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    identification_document = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default=StudentStatus.ACTIVE.value)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ("first_name", "last_name","identification_document","email")