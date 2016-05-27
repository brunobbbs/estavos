# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.models import Tournament


class TournamentDetailTest(TestCase):
    def setUp(self):
        self.obj = Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            description='Campeonato Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 06, 17),
            end_date=date(2016, 06, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 0),
            active=True,
            place='Venâncio Shopping',
            url='http://estavos.com/torneios/irt-brasiliense-de-xadrez-amador-2016-sub-2200/'
        )

    def test_get(self):
        resp = self.client.get(r('tournaments:detail', self.obj.pk))
        # resp = self.client.get('/torneios/irt-brasiliense-de-xadrez-amador-2016')
        self.assertEqual(200, resp.status_code)