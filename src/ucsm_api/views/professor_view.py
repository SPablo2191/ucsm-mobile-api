from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.professor_model import Professor
from ucsm_api.serializers.professor_serializer import ProfessorSerializer
from ucsm_api.models.utils import TableStatus
from ucsm_api.views.utils import TagEnum

@extend_schema(tags=[TagEnum.PROFESSOR.value])
class ProfessorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]
    http_method_names =  ["get","retrieve"]
    pagination_class = LimitOffsetPagination 

    def list(self, request):
        queryset = Professor.objects.filter(status=TableStatus.ACTIVE.value)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = ProfessorSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
