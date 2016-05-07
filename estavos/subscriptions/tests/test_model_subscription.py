# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from estavos.subscriptions.models import Subscription


class LeadModelTest(TestCase):

    def test_create(self):
        Subscription.objects.create(
            first_name='Bruno',
            email='email@test.com',
            is_active=True
        )
        self.assertTrue(Subscription.objects.exists())