from decimal import Decimal

from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.shortcuts import resolve_url as r
from estavos.activities.models import Category, Activity


class ActivityListGet(TestCase):

    def setUp(self):
        category = Category.objects.create(
            name='Coaching',
            value=Decimal('50.00')
        )

        user = get_user_model().objects.create_user(
            email='bruno@email.com',
            username='bruno',
            first_name='Bruno',
            last_name='Barbosa',
            password='123456',
        )

        Activity.objects.create(
            description='Gustavo Medeiros - 01/08',
            date=date(2016, 4, 5),
            transport=Decimal('8.00'),
            partner=user,
            category=category,
            duration=1
        )

        self.client.login(username='bruno', password='123456')
        self.resp = self.client.get(r('activities:list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_require_login(self):
        self.client.logout()
        resp = self.client.get(r('activities:list'))
        self.assertEqual(302, resp.status_code)

    def test_template(self):
        self.assertTemplateUsed('activities/activity_list.html')

    def test_queryset(self):
        self.assertEqual(1, len(self.resp.context['object_list']))