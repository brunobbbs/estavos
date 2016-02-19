# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Inscription(models.Model):

    KLASS = (
        ('children', _('Crianças')),
        ('adults', _('Adultos'))
    )

    PLACES = (
        ('ascade', _('Núcleo de Xadrez do clube ASCADE')),
        ('kumon', _('Kumon Águas Claras - Avenida das Castanheiras'))
    )

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    place = models.CharField(max_length=6, choices=PLACES)
    klass = models.CharField(max_length=8, choices=KLASS)
    student = models.CharField(max_length=150)
    birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name