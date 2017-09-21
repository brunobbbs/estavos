# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from datetime import date, datetime

from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.forms import InscriptionModelForm
from estavos.tournaments.models import Tournament


class NewInscriptionGetValidTest(TestCase):
    def setUp(self):
        self.tournament = Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 6, 17),
            end_date=date(2016, 6, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 00),
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
            start_date=date(2016, 6, 17),
            end_date=date(2016, 6, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 00),
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


class NewInscriptionDateLimit(TestCase):
    def setUp(self):
        self.tournament = Tournament.objects.create(
            title='I Aberto LBX de Xadrez',
            start_date=date(2016, 6, 17),
            end_date=date(2016, 6, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 0),
            active=True,
            place='Núcleo de Xadrez do Clube ASCADE',
            url='http://www.estavos.com/'
        )
        self.resp = self.client.get(r('tournaments:inscription_new', self.tournament.pk), follow=True)

    @unittest.skip('implements this test with mock')
    def test_inscription_date_limit(self):
        """after date limit, inscriptions doesn't more accepted"""
        now = datetime.datetime(2016, 6, 17, 8, 0, 0)
        self.assertRedirects(self.resp, r('tournaments:list'))


class NewInscriptionPostValidTest(TestCase):
    def setUp(self):
        self.tournament = Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 6, 17),
            end_date=date(2016, 6, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 00),
            active=True,
            place='Venâncio Shopping',
            url='http://estavos.com/torneios/irt-brasiliense-de-xadrez-amador-2016-sub-2200/'
        )
        data = {
            'name': 'Bruno Barbosa',
            'email': 'bruno@email.com',
            'birth': date(1989, 12, 18),
            'id_cbx': '39035',
            'id_fide': ''
        }
        self.resp = self.client.post(r('tournaments:inscription_new', self.tournament.pk), data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_send_email(self):
        """after inscription, user must receive a pre-inscription message"""
        self.assertTrue(mail.outbox)
