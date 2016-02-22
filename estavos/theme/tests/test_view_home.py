from django.test import TestCase


class HomeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
