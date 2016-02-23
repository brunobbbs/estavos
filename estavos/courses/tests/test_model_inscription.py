# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, date

from django.test import TestCase

from estavos.courses.models import Inscription, Course


class InscriptionModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='children',
            is_active=True
        )
        self.obj = Inscription.objects.create(
            name='Bruno Barbosa',
            phone='(61) 2222-2222',
            email='bruno@email.com',
            student='Ana Beatriz',
            birth=date(2009, 1, 1),
            course=self.course
        )

    def test_create(self):
        self.assertTrue(Inscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_birth(self):
        self.assertIsInstance(self.obj.birth, date)

    def test_str(self):
        self.assertEqual('Bruno Barbosa', str(self.obj))