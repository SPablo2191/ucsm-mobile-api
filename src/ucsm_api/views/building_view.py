from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models.building_model import Building
from ..serializers.building_serializer import BuildingSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [IsAuthenticated]