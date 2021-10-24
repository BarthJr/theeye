from django.db import models


class Event(models.Model):
    session_id = models.UUIDField()
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    data = models.JSONField()
    timestamp = models.DateTimeField()
