from rest_framework import status, viewsets, mixins
from rest_framework.response import Response

from .tasks import create_event
from .models import Event, EventError
from .filters import EventFilter, EventErrorFilter
from .serializers import EventSerializer, EventErrorSerializer


class EventViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_class = EventFilter

    def create(self, request, *args, **kwargs):
        create_event.delay(request.data)
        return Response(status=status.HTTP_202_ACCEPTED)


class EventErrorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = EventError.objects.all()
    serializer_class = EventErrorSerializer
    filter_class = EventErrorFilter
