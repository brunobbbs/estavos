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
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe seu nome completo'
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
    birth = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: DD/MM/AAAA'
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
    id_cbx = forms.CharField(
        label='ID CBX',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'obrigatório'
            }
        ),
    )
    id_fide = forms.CharField(
        label='ID FIDE',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'se tiver'
            }
        ),
    )


class ConfirmInscriptionForm(forms.Form):
    tournament = forms.ModelChoiceField(
        queryset=Tournament.objects.filter(active=True),
        required=True,
    )
    inscription = forms.ModelChoiceField(
        queryset=Inscription.objects.none(),
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(ConfirmInscriptionForm, self).__init__(*args, **kwargs)
        if 'tournament' in self.data:
            tournament = self.data['tournament']
            if tournament:
                self.fields['inscription'].queryset = Inscription.objects.filter(tournament=tournament)

    def _send_mail(self, subject, to, template_name, context, from_=settings.DEFAULT_FROM_EMAIL):
        body = render_to_string(template_name, context)
        mail.send_mail(subject, body, from_, to)


class InscriptionModelForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ('name', 'email', 'phone')
        exclude = ('tournament', )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Informe seu nome completo')
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Seu melhor email')
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Seu melhor número')
                }
            ),
        }

    def _send_mail(self, subject, to, template_name, context, from_=settings.DEFAULT_FROM_EMAIL):
        body = render_to_string(template_name, context)
        mail.send_mail(subject, body, from_, [from_, to])
