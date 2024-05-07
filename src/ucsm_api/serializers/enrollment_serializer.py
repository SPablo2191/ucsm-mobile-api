from rest_framework import serializers
from ucsm_api.models.enrollment_model import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
        depth = 1