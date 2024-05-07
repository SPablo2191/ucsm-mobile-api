from django.core.exceptions import ObjectDoesNotExist, ValidationError
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.subject_registration_model import SubjectRegistration
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.enrollment_model import Enrollment
from ucsm_api.serializers.subject_registration_serializer import (
    SubjectRegistrationSerializer,
)
from ucsm_api.views.constants import TagEnum


@extend_schema(
    tags=[TagEnum.SUBJECT_REGISTRATION.value],
    parameters=[
        OpenApiParameter(
            name="enrollment_id",
            description="ID of student`s Enrollment",
            type=str,
        ),
        OpenApiParameter(
            name="semester_id",
            description="ID of Current Semester",
            type=str,
        ),
    ],
)
class SubjectRegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubjectRegistration.objects.all()
    serializer_class = SubjectRegistrationSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "retrieve"]
    pagination_class = LimitOffsetPagination

    def list(self, request):
        enrollment_id = request.query_params.get("enrollment_id")
        semester_id = request.query_params.get("semester_id")
        if semester_id is not None:
            return self.get_subjects_of_current_semester(
                enrollment_id=enrollment_id, semester_id=semester_id
            )
        return self.get_subjects_by_enrollment(enrollment_id=enrollment_id)

    def get_subjects_of_current_semester(self, enrollment_id: str, semester_id: str):
        try:
            student_enrollment = Enrollment.objects.get(id=enrollment_id)
            queryset = SubjectRegistration.objects.select_related("subject").filter(
                status=TableStatus.ACTIVE.value,
                enrollment=student_enrollment,
                subject__semester=semester_id,
            )
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = SubjectRegistrationSerializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)
        except ObjectDoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def get_subjects_by_enrollment(self, enrollment_id: str):
        try:
            student_enrollment = Enrollment.objects.get(id=enrollment_id)
            queryset = SubjectRegistration.objects.filter(
                status=TableStatus.ACTIVE.value, enrollment=student_enrollment
            )
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = SubjectRegistrationSerializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)
        except ObjectDoesNotExist:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
