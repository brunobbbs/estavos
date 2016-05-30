# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.models import Inscription, Tournament


class InscriptionDoneTest(TestCase):
    def setUp(self):
        self.tournament = Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 06, 17),
            end_date=date(2016, 06, 19),
            inscriptions_date_limit=datetime(2016, 06, 16, 20, 30, 00),
            active=True,
            place='Venâncio Shopping',
            url='http://estavos.com/torneios/irt-brasiliense-de-xadrez-amador-2016-sub-2200/'
        )
        self.inscription = Inscription.objects.create(
            tournament=self.tournament,
            name='Bruno Barbosa',
            email='email@test.com',
            birth=date(1989, 12, 18),
            id_cbx='39035',
            id_fide='',
            phone='(61) 9999-9999',
        )

    def test_get(self):
        resp = self.client.get(
            r('tournaments:inscription_detail',
              self.tournament.pk,
              self.inscription.slug
            )
        )
        self.assertEqual(200, resp.status_code)

    def test_get_only_tournament_inscriptions(self):
        """ïnscription detail view must return only tournament related inscriptions"""
        t2 = Tournament.objects.create(
            title='I Aberto de Brasília da LBX',
            start_date=date(2016, 05, 26),
            end_date=date(2016, 05, 28),
            inscriptions_date_limit=datetime(2016, 05, 26, 00, 00, 00),
            active=True,
            place='ASCADE',
        )
        resp = self.client.get(
            r('tournaments:inscription_detail',
              t2.pk,
              self.inscription.slug
            )
        )
        self.assertEqual(302, resp.status_code)