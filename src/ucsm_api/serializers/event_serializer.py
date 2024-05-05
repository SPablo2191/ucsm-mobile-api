from rest_framework import serializers
from ucsm_api.models.event_model import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        depth = 1