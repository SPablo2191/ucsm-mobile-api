from rest_framework import serializers
from ucsm_api.models.academic_program_model import AcademicProgram

class AcademicProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicProgram
        fields = "__all__"