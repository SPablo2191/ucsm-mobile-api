from rest_framework import serializers
from ucsm_api.models.debt_model import Debt

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = "__all__"