from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        self._create_event(request.data)

        return Response(status=status.HTTP_202_ACCEPTED)

    def _create_event(self, data):
        serializer = EventSerializer(data=data)
        serializer.is_valid()
        serializer.save()
