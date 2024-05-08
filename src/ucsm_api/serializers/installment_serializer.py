from rest_framework import serializers
from ucsm_api.models.installment_model import Installment

class InstallmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Installment
        fields = "__all__"