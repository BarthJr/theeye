import json

from celery import shared_task

from .models import EventError
from .serializers import EventSerializer


@shared_task
def create_event(data):
    serializer = EventSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
    else:
        EventError.objects.create(data=json.dumps(data), messages=json.dumps(serializer.errors))
