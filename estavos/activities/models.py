# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('Nome', max_length=50)
    value = models.DecimalField('Valor', max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ('name', )

    def __str__(self):
        return '{} - {}'.format(self.name, self.value)


@python_2_unicode_compatible
class Activity(models.Model):
    description = models.CharField('Descrição', max_length=150)
    date = models.DateField('Data')
    transport = models.DecimalField('Transporte', max_digits=7, decimal_places=2)
    partner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Parceiro')
    category = models.ForeignKey('activities.Category', verbose_name='Categoria', related_name='activities')
    duration = models.IntegerField('Duração')

    class Meta:
        verbose_name = 'atividade'
        verbose_name_plural = 'atividades'
        ordering = ('date', )

    def __str__(self):
        return self.description

    def sub_total(self):
        value = self.category.value * self.duration
        subtotal = Decimal(value) + self.transport
        return subtotal