# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, datetime

from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.forms import InscriptionModelForm
from estavos.tournaments.models import Tournament


class NewInscriptionGetValidTest(TestCase):
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
        self.resp = self.client.get(r('tournaments:inscription_new', self.tournament.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_context(self):
        """new_inscription view must be a form on context"""
        self.assertIsInstance(self.resp.context['form'], InscriptionModelForm)


class NewInscriptionGetInvalidTest(TestCase):
    def setUp(self):
        tournament = Tournament.objects.create(
            title='I Aberto LBX de Xadrez',
            start_date=date(2016, 06, 17),
            end_date=date(2016, 06, 19),
            inscriptions_date_limit=datetime(2016, 06, 16, 20, 30, 00),
            active=False,
            place='Núcleo de Xadrez do Clube ASCADE',
            url='http://www.estavos.com/'
        )
        self.resp = self.client.get(r('tournaments:inscription_new', tournament.pk), follow=True)

    def test_redirect_to(self):
        """inactive tournaments inscriptions must redirect to tournaments list page"""
        self.assertRedirects(self.resp, r('tournaments:list'))

    def test_message(self):
        """ïnactive tournaments inscriptions must shows a message to user about it"""
        self.assertContains(self.resp, 'O torneio que você tentou acessar não está ativo.')


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