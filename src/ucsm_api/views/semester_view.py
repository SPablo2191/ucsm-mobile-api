from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.semester_model import Semester
from ucsm_api.serializers.semester_serializer import SemesterSerializer
from ucsm_api.models.utils import TableStatus
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.SEMESTER.value])
class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Semester.objects.filter(status=TableStatus.ACTIVE.value)
        serializer = SemesterSerializer(queryset, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.status = TableStatus.INACTIVE.value
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)