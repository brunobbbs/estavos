# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, date

from django.contrib.auth import get_user_model
from django.core import mail
from django.shortcuts import resolve_url as r
from django.test import TestCase
from estavos.tournaments.models import Inscription, Tournament


class InscriptionsControlConfirmGetTest(TestCase):
    def setUp(self):
        tournament = Tournament.objects.create(
            title='IRT Brasiliense de Xadrez Amador 2016',
            start_date=date(2016, 6, 17),
            end_date=date(2016, 6, 19),
            inscriptions_date_limit=datetime(2016, 6, 16, 20, 30, 00),
            active=True,
            place='Venâncio Shopping',
            url='http://estavos.com/torneios/irt-brasiliense-de-xadrez-amador-2016-sub-2200/'
        )
        inscription = Inscription.objects.create(
            tournament=tournament,
            name='Bruno Barbosa',
            email='email@test.com',
            birth=date(1989, 12, 18),
            id_cbx='39035',
            id_fide='',
            phone='(61) 9999-9999',
            confirmed=False
        )
        Inscription.objects.create(
            tournament=tournament,
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
        self.resp = self.client.get(r('tournaments:inscriptions_control_confirm', tournament.pk, inscription.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_tournament_context(self):
        """view must have a tournament context"""
        self.assertIn('tournament', self.resp.context)


class InscriptionsControlConfirmPostValidTest(TestCase):
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
        self.inscription = Inscription.objects.create(
            tournament=self.tournament,
            name='Bruno Barbosa',
            email='email@test.com',
            birth=date(1989, 12, 18),
            id_cbx='39035',
            id_fide='',
            phone='(61) 9999-9999',
            confirmed=False
        )
        get_user_model().objects.create_superuser(
            username='bruno',
            email='bruno@email.com',
            first_name='Bruno',
            last_name='Barbosa',
            password='123456',
        )
        data = {
            'tournament': self.tournament.pk,
            'inscription': self.inscription.pk
        }
        self.client.login(username='bruno', password='123456')
        self.resp = self.client.post(r('tournaments:inscriptions_control_confirm', self.tournament.pk, self.inscription.pk), data, follow=True)

    def test_post(self):
        """valid post must update confirmed attribute to True"""
        self.assertTrue(Inscription.objects.get(pk=self.inscription.pk).confirmed)

    def test_message(self):
        """success update must shows a success message"""
        self.assertContains(self.resp, 'Inscrição do atleta {0} confirmada com sucesso.'.format(self.inscription.name))

    def test_send_mail(self):
        """after inscription, user must receive a pre-inscription message"""
        self.assertTrue(mail.outbox)


class InscriptionsControlConfirmInvalidGetTest(TestCase):
    def setUp(self):
        self.t_inactive = Tournament.objects.create(
            title='Festival de Xadrez da Família',
            start_date=date(2015, 11, 20),
            end_date=date(2015, 11, 20),
            inscriptions_date_limit=datetime(2015, 11, 19, 23, 59, 00),
            active=False,
            place='Clube ESTAVOS - Brasília',
            url='http://estavos.com/torneios/'
        )
        self.t_active = Tournament.objects.create(
            title='I Aberto de Xadrez Classico LBX/ESTAVOS',
            start_date=date(2016, 11, 20),
            end_date=date(2016, 11, 20),
            inscriptions_date_limit=datetime(2016, 11, 19, 23, 59, 00),
            active=True,
            place='ASCADE',
            url='http://estavos.com/torneios/'
        )
        self.inscription = Inscription.objects.create(
            tournament=self.t_active,
            name='Bruno Barbosa',
            email='email@test.com',
            birth=date(1989, 12, 18),
            id_cbx='39035',
            id_fide='',
            phone='(61) 9999-9999',
            confirmed=False
        )
        get_user_model().objects.create_superuser(
            username='test-super',
            email='test@email.com',
            first_name='Bruno',
            last_name='Barbosa',
            password='123456',
        )
        self.client.login(username='test-super', password='123456')

    def test_get_inactive_tournament(self):
        """view must works only for active tournaments"""
        resp = self.client.get(r('tournaments:inscriptions_control_confirm', self.t_inactive.pk, self.inscription.pk))
        self.assertEqual(302, resp.status_code)

    def test_get_active_tournament_without_login(self):
        """view only can be accessed if user is logged"""
        self.client.logout()
        resp = self.client.get(r('tournaments:inscriptions_control_confirm', self.t_active.pk, self.inscription.pk))
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
        self.client.logout()
        self.client.login(username='bruno', password='123456')
        resp = self.client.get(r('tournaments:inscriptions_control_confirm', self.t_active.pk, self.inscription.pk))
        self.assertEqual(302, resp.status_code)

    def test_update_only_unconfirmed_inscriptions(self):
        """view only updates unconfirmed inscriptions"""
        confirmed_inscription = Inscription.objects.create(
            tournament=self.t_active,
            name='Hugo Ribeiro',
            email='email@test.com',
            birth=date(1992, 3, 16),
            id_cbx='39037',
            id_fide='',
            phone='(61) 9999-9999',
            confirmed=True
        )
        resp = self.client.get(r('tournaments:inscriptions_control_confirm', self.t_active.pk, confirmed_inscription.pk))
        self.assertEqual(302, resp.status_code)
