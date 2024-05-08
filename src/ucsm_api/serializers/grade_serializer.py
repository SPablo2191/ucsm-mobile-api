from rest_framework import serializers
from ucsm_api.models.grade_model import Grade

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"