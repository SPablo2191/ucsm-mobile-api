from rest_framework import serializers
from ucsm_api.models.subject_registration_model import SubjectRegistration

class SubjectRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectRegistration
        fields = "__all__"
        depth = 1