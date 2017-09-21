# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from datetime import datetime, date

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.models import Tournament


class TournamentModelTest(TestCase):

    def setUp(self):
        self.tournament = Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            description='Campeonato Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 6, 17),
            end_date=date(2016, 6, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 00),
            active=True,
            place='Venâncio Shopping',
        )

    def test_create(self):
        self.assertTrue(Tournament.objects.exists())

    def test_str(self):
        self.assertEqual('IRT Brasiliense de Xadrez Amador 2016', str(self.tournament))

    def test_slug(self):
        self.assertTrue(self.tournament.slug)

    def test_get_absolute_url(self):
        url = r('tournaments:detail', self.tournament.pk)
        self.assertEqual(url, self.tournament.get_absolute_url())
