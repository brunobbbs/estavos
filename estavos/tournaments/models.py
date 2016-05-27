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