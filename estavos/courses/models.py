# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Inscription(models.Model):

    KLASS = (
        ('children', _('Crianças')),
        # ('adults', _('Adultos'))
    )

    PLACES = (
        ('kumon', _('Kumon Águas Claras - Avenida das Castanheiras - Início 12/03/2016')),
        # ('ascade', _('Núcleo de Xadrez do clube ASCADE - Início 20/02/2016')),
    )

    name = models.CharField('Nome', max_length=150)
    phone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('Email')
    place = models.CharField('Local', max_length=6, choices=PLACES)
    klass = models.CharField('Turma', max_length=8, choices=KLASS)
    student = models.CharField('Aluno', max_length=150)
    birth = models.DateField('Data de nascimento')
    created_at = models.DateTimeField('Inscrição realizada em', auto_now_add=True)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name