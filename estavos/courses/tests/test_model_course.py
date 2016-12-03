# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from decimal import Decimal

from django.test import TestCase

from estavos.courses.models import Course


class CourseModelTest(TestCase):
    def setUp(self):
        self.obj = Course.objects.create(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2018, 01, 21),
            classes='Crianças',
            price=Decimal('449.70'),
            is_active=True
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_str(self):
        self.assertEqual('Curso APRENDA #3 - 21/01/2018', str(self.obj))

    def test_start_date(self):
        self.assertIsInstance(self.obj.start_date, date)

