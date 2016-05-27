# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Tournament(models.Model):
    title = models.CharField('Nome do evento', max_length=100)
    start_date = models.DateField('Data de início')
    end_date = models.DateField('Data de término')
    inscriptions_date_limit = models.DateTimeField('Data limite para inscrições')
    active = models.BooleanField('Ativo?')
    place = models.CharField('Local', max_length=50)
    url = models.URLField('Link da página do evento')

    def __str__(self):
        return self.title


class Inscription(models.Model):
    tournament = models.ForeignKey('tournaments.Tournament', related_name='inscriptions')
    name = models.CharField('Nome completo', max_length=100)
    email = models.EmailField()
    birth = models.DateField('Data de nascimento')
    id_cbx = models.CharField('ID CBX', max_length=7)
    id_fide = models.CharField('ID FIDE', max_length=7, blank=True)
    phone = models.CharField('Telefone', max_length=15)
    confirmed = models.BooleanField('Confirmado?', default=False)

    def __str__(self):
        return self.name