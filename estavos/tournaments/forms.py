# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from estavos.tournaments.models import Inscription
from django.utils.translation import ugettext_lazy as _


class InscriptionForm(forms.Form):
    name = forms.CharField(
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
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: DD/MM/AAAA'
            }
        ),
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu melhor número'
            }
        ),
    )
    id_cbx = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '(obrigatório)'
            }
        ),
    )
    id_fide = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '(se tiver =))'
            }
        ),
    )


class InscriptionModelForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ('name', 'email', 'birth', 'phone', 'id_cbx', 'id_fide')
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
            'birth': forms.DateInput(
                attrs={'class': 'form-control',
                       'placeholder': _('Ex.: DD/MM/AAAA')
                       }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Seu melhor número')
                }
            ),
            'id_cbx': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('(obrigatório)')
                }
            ),
            'id_fide': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('(se tiver)')
                }
            ),
        }
