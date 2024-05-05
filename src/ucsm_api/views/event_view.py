from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ucsm_api.models.event_model import Event
from ucsm_api.models.utils import TableStatus
from ucsm_api.serializers.event_serializer import EventSerializer
from ucsm_api.views.constants import TagEnum

@extend_schema(tags=[TagEnum.EVENT.value])
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Event.objects.filter(status=TableStatus.ACTIVE.value)
        serializer = EventSerializer(queryset, many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.status = TableStatus.INACTIVE.value
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)