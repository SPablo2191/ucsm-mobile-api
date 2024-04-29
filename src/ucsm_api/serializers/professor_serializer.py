from rest_framework import serializers
from ..models.professor_model import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"