from django.test import TestCase
from django.shortcuts import resolve_url as r


class ActivityListGet(TestCase):
    def test_get(self):
        resp = self.client.get(r('activities:list'))
        self.assertEqual(200, resp.status_code)

    def test_template(self):
        self.assertTemplateUsed('activities/activity_list.html')