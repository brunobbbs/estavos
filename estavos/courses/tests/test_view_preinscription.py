# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.courses.models import Inscription, Course


class PreInscriptionViewGet(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='children',
            is_active=True
        )
        self.obj = Inscription.objects.create(
            name='Bruno Barbosa', phone='(61) 2222-2222', email='bsbruno1@gmail.com',
            student='Ana Beatriz', birth='2009-09-01', course=self.course
        )
        self.resp = self.client.get(r('courses:preinscription', 1))

    def test_get(self):
        """'courses:thanks' pattern should return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/preinscription.html')

    def test_html(self):
        contents = [self.obj.name, 'KUMON AGUAS CLARAS', 'CRIANÇAS', self.obj.student]
        for expected in contents:
            self.assertContains(self.resp, expected)