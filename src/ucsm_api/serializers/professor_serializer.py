from rest_framework import serializers
from ucsm_api.models.professor_model import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"