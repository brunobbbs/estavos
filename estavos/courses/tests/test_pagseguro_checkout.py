# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.courses.models import Inscription, Course


class PagseguroCheckoutRedirect(TestCase):
    def setUp(self):
        course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 3, 12),
            classes='Crianças',
            is_active=True
        )
        self.obj = Inscription.objects.create(
            name='Bruno Barbosa',
            phone='(61) 2222-2222',
            email='bruno@email.com',
            student='Ana Beatriz',
            birth=date(2009, 1, 1),
            course=course
        )

    def test_get(self):
        resp = self.client.get(r('courses:checkout', self.obj.slug))
        self.assertEqual(302, resp.status_code)
