# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.models import Tournament


class NewInscriptionTest(TestCase):
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

    def test_get(self):
        resp = self.client.get(r('tournaments:inscription_new', self.tournament.pk))
        self.assertEqual(200, resp.status_code)


class NewInscriptionPostValidTest(TestCase):
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

    def test_post(self):
        data = {
            'name': 'Bruno Barbosa',
            'email': 'bruno@email.com',
            'birth': date(1989, 12, 18),
            'id_cbx': '39035',
            'id_fide': ''
        }
        resp = self.client.post(r('tournaments:inscription_new', self.tournament.pk), data)
        self.assertEqual(302, resp.status_code)