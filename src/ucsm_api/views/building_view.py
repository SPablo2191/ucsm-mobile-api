from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.building_model import Building
from ucsm_api.models.utils import TableStatus
from ucsm_api.serializers.building_serializer import BuildingSerializer
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.BUILDING.value])
class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get","retrieve"]
    pagination_class = LimitOffsetPagination 

    def list(self, request):
        queryset = Building.objects.filter(status=TableStatus.ACTIVE.value)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = BuildingSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
