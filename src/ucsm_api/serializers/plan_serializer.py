from rest_framework import serializers
from ucsm_api.models.plan_model import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"