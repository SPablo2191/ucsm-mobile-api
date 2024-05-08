from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action

from ucsm_api.models.subject_model import Subject
from ucsm_api.serializers.subject_serializer import SubjectSerializer
from ucsm_api.views.utils import TagEnum

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
class SubjectView(viewsets.generics):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "retrieve"]
    pagination_class = LimitOffsetPagination