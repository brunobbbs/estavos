# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from estavos.utils.slug import unique_slugify
from django.utils.encoding import python_2_unicode_compatible
from django.shortcuts import resolve_url as r


@python_2_unicode_compatible
class Tournament(models.Model):
    title = models.CharField('Nome do evento', max_length=100)
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de início')
    end_date = models.DateField('Data de término')
    inscriptions_date_limit = models.DateTimeField('Data limite para inscrições')
    active = models.BooleanField('Ativo?')
    place = models.CharField('Local', max_length=50)
    url = models.URLField('Link da página do evento', blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('tournaments:detail', self.pk)

    def save(self, **kwargs):
        unique_slugify(self, self.title)
        super(Tournament, self).save(**kwargs)


@python_2_unicode_compatible
class Inscription(models.Model):
    tournament = models.ForeignKey('tournaments.Tournament', related_name='inscriptions')
    name = models.CharField('Nome completo', max_length=100)
    email = models.EmailField()
    birth = models.DateField('Data de nascimento')
    id_cbx = models.CharField('ID CBX', max_length=7)
    id_fide = models.CharField('ID FIDE', max_length=7, blank=True)
    phone = models.CharField('Telefone', max_length=15, blank=True)
    confirmed = models.BooleanField('Confirmado?', default=False)
    slug = models.SlugField('Cod. Inscrição', max_length=32, unique=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        import uuid
        slug = uuid.uuid4().get_hex()
        unique_slugify(self, slug)
        super(Inscription, self).save(**kwargs)