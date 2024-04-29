from rest_framework import serializers
from ..models.student_model import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["identification_document","password"]