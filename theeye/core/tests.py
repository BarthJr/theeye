import datetime

from rest_framework.test import APITestCase

from .models import EventError


class EventTest(APITestCase):
    def setUp(self):
        self.events = self._getEvents()

    def test_list_events(self):
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, 200)

    def test_create_event(self):
        for event in self.events:
            response = self.client.post('/api/events/', event, format='json')
            self.assertEqual(response.status_code, 202)

    def test_create_event_with_future_timestamp_should_create_event_error(self):
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        event = self.events[0]
        event['timestamp'] = tomorrow

        self.client.post('/api/events/', event, format='json')
        self.assertTrue(EventError.objects.exists())

    def _getEvents(self):
        return [
            {
                "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                "category": "page interaction",
                "name": "pageview",
                "data": {
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                },
                "timestamp": "2021-01-01 09:15:27.243860"
            },
            {
                "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                "category": "page interaction",
                "name": "cta click",
                "data": {
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                    "element": "chat bubble"
                },
                "timestamp": "2021-01-01 09:15:27.243860"
            },
            {
                "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
                "category": "form interaction",
                "name": "submit",
                "data": {
                    "host": "www.consumeraffairs.com",
                    "path": "/",
                    "form": {
                        "first_name": "John",
                        "last_name": "Doe"
                    }
                },
                "timestamp": "2021-01-01 09:15:27.243860"
            },
        ]
