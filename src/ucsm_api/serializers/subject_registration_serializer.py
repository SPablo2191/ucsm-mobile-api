from rest_framework import serializers
from ucsm_api.models.subject_registration_model import SubjectRegistration
from ucsm_api.models.student_commission_model import StudentCommission
from ucsm_api.serializers.student_commission_serializer import StudentCommissionSerializer

class SubjectRegistrationSerializer(serializers.ModelSerializer):
    student_commissions = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = SubjectRegistration
        fields = "__all__"
        depth = 1
    def get_student_commissions(self,subject_registration):
        selected_installments = StudentCommission.objects.filter(subject_registration = subject_registration)
        return StudentCommissionSerializer(selected_installments, many=True).data