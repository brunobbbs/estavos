# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from estavos.leads.models import Lead


class LeadModelTest(TestCase):

    def test_create(self):
        Lead.objects.create(
            first_name='Bruno',
            email='email@test.com',
            is_active=True
        )
        self.assertTrue(Lead.objects.exists())