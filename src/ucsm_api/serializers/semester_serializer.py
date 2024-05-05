from rest_framework import serializers
from ucsm_api.models.semester_model import Semester

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = "__all__"