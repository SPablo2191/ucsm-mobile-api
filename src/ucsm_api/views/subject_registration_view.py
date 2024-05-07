from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.subject_registration_model import SubjectRegistration
from ucsm_api.models.utils import TableStatus
from ucsm_api.serializers.subject_registration_serializer import SubjectRegistrationSerializer
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.SUBJECT_REGISTRATION.value])
class SubjectRegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubjectRegistration.objects.all()
    serializer_class = SubjectRegistrationSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get","retrieve"]
    pagination_class = LimitOffsetPagination 

    def list(self, request):
        queryset = SubjectRegistration.objects.filter(status=TableStatus.ACTIVE.value)
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = SubjectRegistrationSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
