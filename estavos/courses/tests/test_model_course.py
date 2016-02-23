# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.test import TestCase
from estavos.courses.models import Course


class CourseModelTest(TestCase):
    def setUp(self):
        self.obj = Course(
            name='Curso APRENDA #3',
            place='Kumon Águas Claras - Av. das Castanheiras',
            start_date=date(2016, 03, 12),
            classes='Crianças',
            is_active=True
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_str(self):
        self.assertEqual('Curso APRENDA #3 - 12/03/2016', str(self.obj))

    def test_start_date(self):
        self.assertIsInstance(self.obj.start_date, date)