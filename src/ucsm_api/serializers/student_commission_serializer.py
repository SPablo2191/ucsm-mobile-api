from rest_framework import serializers
from ucsm_api.models.student_commission_model import StudentCommission
from ucsm_api.models.grade_model import Grade
from ucsm_api.serializers.grade_serializer import GradeSerializer

class StudentCommissionSerializer(serializers.ModelSerializer):
    grades = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = StudentCommission
        fields = "__all__"
        depth = 3
    def get_grades(self,student_commision):
        selected_grades = Grade.objects.filter(student_commision = student_commision)
        return GradeSerializer(selected_grades, many=True).data