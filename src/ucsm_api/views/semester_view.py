from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.semester_model import Semester
from ..serializers.semester_serializer import SemesterSerializer
from ..models.utils import TableStatus
from rest_framework import status

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