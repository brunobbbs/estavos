# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, date

from django.contrib.auth import get_user_model
from django.test import TestCase
from estavos.tournaments.models import Inscription, Tournament


class InscriptionsControlViewTest(TestCase):
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
        Inscription.objects.create(
            tournament=self.tournament,
            name='Hugo Ribeiro',
            email='email@test.com',
            birth=date(1992, 03, 16),
            id_cbx='39034',
            id_fide='',
            phone='(61) 9999-9999',
        )
        Inscription.objects.create(
            tournament=self.tournament,
            name='Bruno Barbosa',
            email='email@test.com',
            birth=date(1989, 12, 18),
            id_cbx='39035',
            id_fide='',
            phone='(61) 9999-9999',
            confirmed=True
        )
        get_user_model().objects.create_superuser(
            username='bruno',
            email='bruno@email.com',
            first_name='Bruno',
            last_name='Barbosa',
            password='123456',
        )
        self.client.login(username='bruno', password='123456')
        self.resp = self.client.get('/torneios/1/controle/inscricoes/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_tournament_context(self):
        """view must have a tournament context"""
        self.assertIn('tournament', self.resp.context)

    def test_unconfirmed_inscriptions(self):
        """view must return unconfirmed inscriptions"""
        self.assertEqual(1, len(self.resp.context['object_list']))


class InscriptionsControlInvalidGetTest(TestCase):
    def setUp(self):
        Tournament.objects.create(
            title='Festival de Xadrez da Família',
            start_date=date(2015, 11, 20),
            end_date=date(2015, 11, 20),
            inscriptions_date_limit=datetime(2015, 11, 19, 23, 59, 00),
            active=False,
            place='Clube ESTAVOS - Brasília',
            url='http://estavos.com/torneios/'
        )
        Tournament.objects.create(
            title='I Aberto de Xadrez Classico LBX/ESTAVOS',
            start_date=date(2016, 11, 20),
            end_date=date(2016, 11, 20),
            inscriptions_date_limit=datetime(2016, 11, 19, 23, 59, 00),
            active=True,
            place='ASCADE',
            url='http://estavos.com/torneios/'
        )

    def test_get_inactive_tournament(self):
        """view must works only for active tournaments"""
        resp = self.client.get('/torneios/1/controle/inscricoes/')
        self.assertEqual(302, resp.status_code)

    def test_get_active_tournament_without_login(self):
        """view only can be accessed if user is logged"""
        resp = self.client.get('/torneios/2/controle/inscricoes/')
        self.assertEqual(302, resp.status_code)

    def test_get_without_admin(self):
        """view can be accessed only for admin users"""
        get_user_model().objects.create_user(
            username='bruno',
            email='bruno@email.com',
            first_name='Bruno',
            last_name='Barbosa',
            password='123456',
        )
        self.client.login(username='bruno', password='123456')
        resp = self.client.get('/torneios/2/controle/inscricoes/')
        self.assertEqual(302, resp.status_code)