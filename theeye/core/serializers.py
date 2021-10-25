from django.utils import timezone
from rest_framework import serializers

from .models import Event, EventError


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_timestamp(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("timestamp field is in the future")

        return value

    def validate_data(self, value):
        if not value:
            raise serializers.ValidationError("data field is empty")
        if not isinstance(value, dict):
            raise serializers.ValidationError("data field is not a valid JSON")

        return value


class EventErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventError
        fields = '__all__'
