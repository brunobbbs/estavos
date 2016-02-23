# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.courses.models import Inscription, Course


class InscriptionDetailGet(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='Crianças',
            is_active=True
        )
        self.obj = Inscription.objects.create(
            name='Bruno Barbosa', phone='(61) 2222-2222', email='bsbruno1@gmail.com',
            student='Ana Beatriz', birth='2009-09-01', course=self.course
        )
        self.resp = self.client.get(r('courses:inscription_detail', self.obj.slug))

    def test_get(self):
        """'courses:thanks' pattern should return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'courses/inscription_detail.html')

    def test_html(self):
        contents = [self.obj.name, self.course.place, self.course.classes, self.obj.student]
        for expected in contents:
            self.assertContains(self.resp, expected)