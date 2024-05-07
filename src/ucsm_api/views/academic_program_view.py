from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.academic_program_model import AcademicProgram
from ucsm_api.models.utils import TableStatus
from ucsm_api.serializers.academic_program_serializer import AcademicProgramSerializer
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.ACADEMIC_PROGRAM.value])
class AcademicProgramViewSet(viewsets.ModelViewSet):
    queryset = AcademicProgram.objects.all()
    serializer_class = AcademicProgramSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    pagination_class = LimitOffsetPagination 

    def list(self, request):
        queryset = AcademicProgram.objects.filter(status=TableStatus.ACTIVE.value)
        print(str(queryset.query))
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = AcademicProgramSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
    # def destroy(self, request, pk=None):
    #     instance = self.get_object()
    #     instance.status = TableStatus.INACTIVE.value
    #     instance.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)