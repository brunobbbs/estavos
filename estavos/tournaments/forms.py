# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.core import mail
from django.template.loader import render_to_string
from estavos.tournaments.models import Inscription, Tournament
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class InscriptionForm(forms.Form):
    name = forms.CharField(
        label='Nome do responsável',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o nome do responsável pelo(s) atleta(s)'
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu melhor email'
            }
        ),
    )
    phone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu melhor número'
            }
        ),
    )

    def _send_mail(self, subject, to, template_name, context, from_=settings.DEFAULT_FROM_EMAIL):
        body = render_to_string(template_name, context)
        mail.send_mail(subject, body, from_, to)


class CompetitorForm(forms.Form):
    name = forms.CharField(label='Nome do atleta')
    birth = forms.DateField(label='Data de nascimento')
    club = forms.CharField(label='Clube/Escola', required=False)
    id_lbx = forms.CharField(label='ID LBX', required=False)
    id_fide = forms.CharField(label='ID FIDE', required=False)


CompetitorFormSet = forms.formset_factory(CompetitorForm, extra=1, min_num=1, validate_min=True)
