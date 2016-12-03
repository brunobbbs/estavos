# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase


class HomeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('courses:home'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/index.html')

    def test_next_course_on_context(self):
        self.assertIn('next_course', self.resp.context)
