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

        admin = get_user_model().objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='123456',
        )

        user = get_user_model().objects.create_user(
            username='bruno',
            email='bruno@email.com',
            first_name='Bruno',
            last_name='Barbosa',
            password='123456',
        )

        user2 = get_user_model().objects.create_user(
            username='hugo',
            email='hugo@email.com',
            first_name='Hugo',
            last_name='Ribeiro',
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

        Activity.objects.create(
            description='Fabio Alexandre - 02/08',
            date=date(2016, 4, 1),
            transport=Decimal('8.00'),
            partner=user2,
            category=category,
            duration=1
        )

        self.client.login(username='hugo', password='123456')
        self.resp = self.client.get(r('activities:list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_require_login(self):
        self.client.logout()
        resp = self.client.get(r('activities:list'))
        self.assertEqual(302, resp.status_code)

    def test_template(self):
        self.assertTemplateUsed('activities/activity_list.html')

    def test_partner_view(self):
        """partner can view only your own activities"""
        self.assertEqual(1, len(self.resp.context['object_list']))

    def test_admin_view(self):
        """admin can view all user activities"""
        self.client.logout()
        self.client.login(username='admin', password='123456')
        resp = self.client.get(r('activities:list'))
        self.assertEqual(2, len(resp.context['object_list']))