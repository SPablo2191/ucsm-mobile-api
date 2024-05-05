from rest_framework import serializers
from ucsm_api.models.building_model import Building

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"