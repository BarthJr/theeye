from django.db import models


class Event(models.Model):
    session_id = models.UUIDField()
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']


class EventError(models.Model):
    data = models.TextField()
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
