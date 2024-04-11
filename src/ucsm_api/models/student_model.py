from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib import admin
from django.db import models
from django.utils import timezone

from datetime import date
from enum import Enum
import uuid


class StudentStatus(Enum):
    """
    Use to filter per student status
    Return:
    ACTIVE => It has an active enrollment
    INACTIVE => It doesnt have any active enrollment
    SUSPENDED => It is a block student
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"


class StudentManager(UserManager):
    def _create_user(self, identification_document, email, password, **extra_fields):
        if not identification_document:
            raise ValueError("You have not provided a valid identification document")
        email = self.normalize_email(email)
        user = self.model(
            identification_document=identification_document, email=email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, identification_document=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            identification_document, email, password, **extra_fields
        )

    def create_superuser(
        self, identification_document=None, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(
            identification_document, email, password, **extra_fields
        )


class Student(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    first_name = models.CharField(max_length=150, blank=True, default="")
    middle_name = models.CharField(max_length=150, blank=True, default="")
    last_name = models.CharField(max_length=150, blank=True, default="")
    second_last_name = models.CharField(max_length=150, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    birth_date = models.DateField(default=date.today)
    phone_number = models.CharField(max_length=20, blank=True, default="")
    address = models.TextField(blank=True, default="")
    identification_document = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, default=StudentStatus.ACTIVE.value)
    register_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = StudentManager()
    USERNAME_FIELD = "identification_document"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name or self.identification_document

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("identification_document", "first_name", "last_name", "email")
