# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Course(models.Model):
    CLASSES = (
        ('children', _('Crianças')),
        ('adults', _('Adultos'))
    )

    name = models.CharField('Nome', max_length=150)
    place = models.CharField('Local', max_length=100)
    start_date = models.DateField('Data de início')
    classes = models.CharField('Turmas', max_length=15, choices=CLASSES)
    is_active = models.BooleanField('Ativo?', default=False)

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ('start_date', )

    def __str__(self):
        return '{} - {}'.format(self.name, self.start_date.strftime('%d/%m/%Y'))


@python_2_unicode_compatible
class Inscription(models.Model):
    name = models.CharField('Nome', max_length=150)
    phone = models.CharField('Telefone', max_length=15)
    email = models.EmailField('Email')
    student = models.CharField('Aluno', max_length=150)
    birth = models.DateField('Data de nascimento')
    created_at = models.DateTimeField('Inscrição realizada em', auto_now_add=True)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
