# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.courses.models import Inscription


class PreInscriptionViewGet(TestCase):
    def setUp(self):
        self.obj = Inscription.objects.create(
            name='Bruno Barbosa', phone='(61) 2222-2222', email='bsbruno1@gmail.com', place='kumon',
            klass='adults', student='Ana Beatriz', birth='2009-09-01'
        )
        self.resp = self.client.get(r('courses:preinscription', 1))

    def test_get(self):
        """'courses:thanks' pattern should return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/preinscription.html')

    def test_html(self):
        contents = [self.obj.name, self.obj.get_place_display(), self.obj.get_klass_display(), self.obj.student]
        for expected in contents:
            self.assertContains(self.resp, expected)