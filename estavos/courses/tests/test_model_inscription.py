# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.test import TestCase

from estavos.courses.models import Inscription


class InscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Inscription(
            name='Bruno Barbosa',
            phone='(61) 2222-2222',
            email='bruno@email.com',
            place='ascade',
            klass='children',
            student='Ana Beatriz',
            birth='2009-01-01'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Inscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Bruno Barbosa', str(self.obj))