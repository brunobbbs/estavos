from __future__ import unicode_literals

from datetime import date

from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from estavos.activities.models import Activity, Category


class ActivityModelTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            username='valcarcel',
            first_name='Carlos',
            last_name='Valcarcel',
            email='carlos@estavos.com',
            password='xadrez'
        )
        category = Category.objects.create(
            name='Coaching',
            value=Decimal('50.00')
        )
        self.obj = Activity.objects.create(
            description='Gustavo Medeiros - 01/08',
            date=date(2016, 2, 23),
            transport=Decimal('8.00'),
            partner=user,
            category=category,
            duration=2
        )

    def test_create(self):
        self.assertTrue(Activity.objects.exists())

    def test_str(self):
        self.assertEqual('Gustavo Medeiros - 01/08', str(self.obj))

    def test_subtotal(self):
        """subtotal must returns a result of category value and activity transporte times activity duration"""
        self.assertEqual(Decimal('108.00'), self.obj.sub_total())
