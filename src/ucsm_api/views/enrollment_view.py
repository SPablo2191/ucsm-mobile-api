from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status, serializers
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.views.constants import TagEnum
from ucsm_api.models.utils import TableStatus
from ucsm_api.models.enrollment_model import Enrollment
from ucsm_api.models.student_model import Student
from ucsm_api.serializers.enrollment_serializer import EnrollmentSerializer

@extend_schema(
    tags=[TagEnum.ENROLLMENT.value],
    parameters=[
            OpenApiParameter(name='identification_document', description='DNI', type=str),
        ]
)
class EnrollmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get","retrieve"]
    pagination_class = LimitOffsetPagination

    def list(self, request):
        try:
            identification_document = request.query_params.get("identification_document")
            student = Student.objects.get(
                identification_document=identification_document
            )
            queryset = Enrollment.objects.filter(
                status=TableStatus.ACTIVE.value, student=student
            )
            paginated_queryset = self.paginate_queryset(queryset)
            serializer = EnrollmentSerializer(paginated_queryset, many=True)
            return self.get_paginated_response(serializer.data)
        except ObjectDoesNotExist:
            return Response(
                {"error": "El usuario no dispone de enrollments."},
                status=status.HTTP_404_NOT_FOUND,
            )

