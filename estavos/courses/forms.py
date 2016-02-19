# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core import mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from estavos.courses.models import Inscription


class InscriptionForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ('name', 'phone', 'email', 'place', 'klass', 'student', 'birth')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Informe seu nome')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Informe um telefone de contato')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Enviaremos informações adicionais sobre a inscrição por email')}),
            'place': forms.Select(attrs={'class': 'form-control'}),
            'klass': forms.Select(attrs={'class': 'form-control'}),
            'student': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Qual o nome do aluno?')}),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': _('Informe a data de nascimento do aluno Formato: dd/mm/aaaa')}),
        }

    def send_mail(self, subject, from_, to, template_name, context):
         body = render_to_string(template_name, context)
         mail.send_mail(subject, body, from_, [to, ])
