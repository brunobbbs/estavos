from django.test import TestCase
from django.shortcuts import resolve_url as r


class ThanksViewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('courses:thanks'))

    def test_get(self):
        """'courses:thanks' pattern should return status code 200"""
        self.assertEqual(200, self.resp.status_code)