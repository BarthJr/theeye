from rest_framework.test import APITestCase


class EventTest(APITestCase):
    def test_list_events(self):
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, 200)
