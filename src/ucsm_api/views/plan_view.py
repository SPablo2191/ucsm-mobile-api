from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.plan_model import Plan
from ucsm_api.models.utils import TableStatus
from ucsm_api.serializers.plan_serializer import PlanSerializer
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.PLAN.value])
class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get","retrieve"]
    pagination_class = LimitOffsetPagination 

    def list(self, request):
        queryset = Plan.objects.filter(status=TableStatus.ACTIVE.value)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = PlanSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
    
