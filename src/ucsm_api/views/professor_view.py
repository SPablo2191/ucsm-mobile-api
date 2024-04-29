from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.professor_model import Professor
from ..serializers.professor_serializer import ProfessorSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]