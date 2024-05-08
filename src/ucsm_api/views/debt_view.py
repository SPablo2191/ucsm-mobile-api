from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.debt_model import Debt
from ucsm_api.models.installment_model import Installment
from ucsm_api.models.utils import TableStatus
from ucsm_api.serializers.debt_serializer import DebtSerializer
from ucsm_api.views.utils import TagEnum


@extend_schema(
    tags=[TagEnum.DEBT.value],
    parameters=[
        OpenApiParameter(
            name="enrollment_id",
            description="ID of student`s Enrollment",
            type=str,
            required=True
        )
    ],
)
class DebtViewSet(viewsets.GenericViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "retrieve"]
    pagination_class = LimitOffsetPagination
    @action(methods=["GET"], detail=False)
    def get_debt(self, request):
        enrollment_id = request.query_params.get("enrollment_id")
        queryset = Debt.objects.filter(status=TableStatus.ACTIVE.value)
        queryset = Debt.objects.filter(status=TableStatus.ACTIVE.value, enrollment = enrollment_id)
        debt = get_object_or_404(queryset, enrollment=enrollment_id)
        serializer = DebtSerializer(debt)
        return Response(serializer.data,status=status.HTTP_200_OK)



