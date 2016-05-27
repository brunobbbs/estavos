# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, date

from django.test import TestCase
from estavos.tournaments.models import Tournament


class TournamentModelTest(TestCase):

    def setUp(self):
        self.tournament = Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            description='Campeonato Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 06, 17),
            end_date=date(2016, 06, 19),
            inscriptions_date_limit=datetime(2016, 06, 16, 20, 30, 00),
            active=True,
            place='Venâncio Shopping',
            url='http://estavos.com/torneios/irt-brasiliense-de-xadrez-amador-2016-sub-2200/'
        )

    def test_create(self):
        self.assertTrue(Tournament.objects.exists())

    def test_str(self):
        self.assertEqual('IRT Brasiliense de Xadrez Amador 2016', str(self.tournament))

    def test_slug(self):
        self.assertTrue(self.tournament.slug)