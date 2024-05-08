from rest_framework import serializers
from ucsm_api.models.subject_model import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"