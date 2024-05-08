from rest_framework import serializers
from ucsm_api.models.debt_model import Debt
from ucsm_api.models.installment_model import Installment
from ucsm_api.serializers.installment_serializer import InstallmentSerializer

class DebtSerializer(serializers.ModelSerializer):
    installments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Debt
        fields = "__all__"
    def get_installments(self,debt):
        selected_installments = Installment.objects.filter(debt = debt)
        return InstallmentSerializer(selected_installments, many=True).data
