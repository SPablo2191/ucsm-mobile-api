from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from ucsm_api.models.semester_model import Semester
from ucsm_api.serializers.semester_serializer import SemesterSerializer
from ucsm_api.models.utils import TableStatus
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.SEMESTER.value])
class SemesterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated]
    http_method_names =  ["get","retrieve"]
    pagination_class = LimitOffsetPagination 

    def list(self, request):
        queryset = Semester.objects.filter(status=TableStatus.ACTIVE.value)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = SemesterSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
