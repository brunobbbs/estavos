# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext as _


class InscriptionForm(forms.Form):
    KLASS = (
        ('children', _('Crianças')),
        ('adults', _('Adultos'))
    )
    PLACES = (
        ('ascade', _('Núcleo de Xadrez do clube ASCADE')),
        ('kumon', _('Kumon Águas Claras - Avenida das Castanheiras'))
    )

    name = forms.CharField(
        label=_('Nome'),
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Informe seu nome')}
        ),
        max_length=150
    )
    phone = forms.CharField(
        label=_('Telefone'),
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Informe um telefone de contato')}
        ),
        max_length=15
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': _('Enviaremos informações adicionais sobre a inscrição por email')}
        ),
    )
    place = forms.ChoiceField(
        label=_('Local'),
        help_text=_('Escolha o local que você deseja realizar o curso'),
        choices=PLACES,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        )
    )
    klass = forms.ChoiceField(
        label=_('Turma'),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        help_text=_('Deseja efetuar a inscrição em qual turma?'),
        choices=KLASS
    )
    student = forms.CharField(
        label=_('Nome do aluno'),
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Qual o nome do aluno?'}
        ),
        max_length=150
    )
    birth = forms.DateField(
        label=_('Data de nascimento'),
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': 'Informe a data de nascimento do aluno'}
        )
    )
