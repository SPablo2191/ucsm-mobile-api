from rest_framework import serializers
from ..models.building_model import Building

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"