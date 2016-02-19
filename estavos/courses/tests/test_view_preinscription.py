# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import resolve_url as r
from django.test import TestCase


class PreInscriptionViewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('courses:preinscription'))

    def test_get(self):
        """'courses:thanks' pattern should return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/preinscription.html')
