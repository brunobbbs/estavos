# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.models import Tournament


class TournamentListTest(TestCase):
    def setUp(self):
        Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            description='Campeonato Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 06, 17),
            end_date=date(2016, 06, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 0),
            active=True,
            place='Venâncio Shopping',
            url='http://estavos.com/torneios/irt-brasiliense-de-xadrez-amador-2016-sub-2200/'
        )
        Tournament.objects.create(
            title='I Aberto LBX de Xadrez Clássico',
            description='Torneio clássico de Xadrez da LBX',
            start_date=date(2016, 05, 26),
            end_date=date(2016, 05, 28),
            inscriptions_date_limit=datetime(2016, 05, 26, 9, 0, 0),
            active=False,
            place='ASCADE',
            url='http://estavos.com/'
        )
        self.resp = self.client.get(r('tournaments:list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_active_tournaments(self):
        """default list view must returns only active tournaments"""
        self.assertEqual(1, len(self.resp.context['object_list']))

    def test_inactive_tournaments(self):
        self.assertEqual(1, len(self.resp.context['inactive_tournaments']))

