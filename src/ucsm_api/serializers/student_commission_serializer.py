from rest_framework import serializers
from ucsm_api.models.student_commission_model import StudentCommission

class StudentCommissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCommission
        fields = "__all__"
        depth = 3