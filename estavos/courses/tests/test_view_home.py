from django.core.urlresolvers import reverse
from django.test import TestCase


class HomeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('courses:home'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/index.html')