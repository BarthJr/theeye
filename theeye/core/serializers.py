from django.utils import timezone
from rest_framework import serializers

from .models import Event, EventError


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_timestamp(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("timestamp is in the future")

        return value


class EventErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventError
        fields = '__all__'
