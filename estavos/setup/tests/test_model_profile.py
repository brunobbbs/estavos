# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from ..models import UserProfile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='bruno',
            first_name='Bruno',
            last_name='Barbosa',
            email='bruno@estavos.com',
            password='xadrez'
        )

    def test_create(self):
        self.assertTrue(UserProfile.objects.exists())

    def test_str(self):
        self.assertEqual('Bruno Barbosa', str(self.user.profile))