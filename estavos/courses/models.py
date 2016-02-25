# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.shortcuts import resolve_url as r
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from estavos.utils.slug import unique_slugify


@python_2_unicode_compatible
class Course(models.Model):
    name = models.CharField('Nome', max_length=150)
    place = models.CharField('Local', max_length=100)
    start_date = models.DateField('Data de início')
    classes = models.CharField('Turmas', max_length=50)
    is_active = models.BooleanField('Ativo?', default=False)
    price = models.DecimalField('Preço', max_digits=6, decimal_places=2, default=Decimal('449.70'))

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
    course = models.ForeignKey('courses.Course', verbose_name='Curso', related_name='inscriptions')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at', )

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        import uuid
        slug = uuid.uuid4().get_hex()
        unique_slugify(self, slug)
        super(Inscription, self).save(**kwargs)

    def get_absolute_url(self):
        return r('courses:inscription_detail', slug=self.slug)