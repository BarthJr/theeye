import json

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Event, EventError
from .serializers import EventSerializer, EventErrorSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        self._create_event(request.data)
        return Response(status=status.HTTP_202_ACCEPTED)

    def _create_event(self, data):
        serializer = EventSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
        else:
            EventError.objects.create(data=json.dumps(data), messages=json.dumps(serializer.errors))


class EventErrorViewSet(viewsets.ModelViewSet):
    queryset = EventError.objects.all()
    serializer_class = EventErrorSerializer
