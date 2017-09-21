# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, date

from decimal import Decimal

from django.shortcuts import resolve_url as r
from django.test import TestCase

from estavos.courses.models import Inscription, Course


class InscriptionModelTest(TestCase):
    def setUp(self):
        course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 3, 12),
            classes='Crianças',
            is_active=True,
            price=Decimal('449.70')
        )
        self.obj = Inscription.objects.create(
            name='Bruno Barbosa',
            phone='(61) 2222-2222',
            email='bruno@email.com',
            student='Ana Beatriz',
            birth=date(2009, 1, 1),
            course=course
        )

    def test_create(self):
        self.assertTrue(Inscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_birth(self):
        self.assertIsInstance(self.obj.birth, date)

    def test_str(self):
        self.assertEqual('Bruno Barbosa', str(self.obj))

    def test_get_absolute_url(self):
        url = r('courses:inscription_detail', slug=self.obj.slug)
        self.assertEqual(url, self.obj.get_absolute_url())
