from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from ucsm_api.models.academic_program_model import AcademicProgram
from ucsm_api.models.utils import TableStatus
from ucsm_api.serializers.academic_program_serializer import AcademicProgramSerializer
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.ACADEMIC_PROGRAM.value])
class AcademicProgramViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AcademicProgram.objects.all()
    serializer_class = AcademicProgramSerializer
    permission_classes = [IsAuthenticated]
    http_method_names =  ["get","retrieve"]
    pagination_class = LimitOffsetPagination 

    def list(self, request):
        queryset = AcademicProgram.objects.filter(status=TableStatus.ACTIVE.value)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = AcademicProgramSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
