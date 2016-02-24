from __future__ import unicode_literals

from decimal import Decimal

from django.test import TestCase
from estavos.activities.models import Category


class CategoryModelTest(TestCase):
    def setUp(self):
        self.obj = Category.objects.create(
            name='Coaching',
            value=Decimal('50.00')
        )

    def test_create(self):
        self.assertTrue(Category.objects.exists())

    def test_str(self):
        self.assertEqual('Coaching - 50.00', str(self.obj))