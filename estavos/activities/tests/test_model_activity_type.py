from __future__ import unicode_literals

from decimal import Decimal

from django.test import TestCase


class ActivityTypeModelTest(TestCase):
    def test_create(self):
        obj = ActivityType(
            name='Coaching',
            value=Decimal('50.00')
        )
        self.assertTrue(ActivityType.objects.exists())