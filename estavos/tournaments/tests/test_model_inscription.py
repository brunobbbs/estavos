# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, date

from django.test import TestCase
from estavos.tournaments.models import Inscription, Tournament


class InscriptionModelTest(TestCase):

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
        )

    def test_create(self):
        self.assertTrue(Inscription.objects.exists())

    def test_str(self):
        self.assertEqual('Bruno Barbosa', str(self.inscription))

    def test_inscription_slug(self):
        self.assertTrue(self.inscription.slug)
