# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _
from estavos.courses.models import Inscription


class InscriptionForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ('name', 'phone', 'email', 'student', 'birth')
        exclude = ('course', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Informe seu nome')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Informe um telefone de contato')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Enviaremos informações adicionais sobre a inscrição por email')}),
            'student': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Qual o nome do aluno?')}),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': _('Informe a data de nascimento do aluno Formato: dd/mm/aaaa')}),
        }

    def send_mail(self, subject, from_, to, template_name, context):
        body = render_to_string(template_name, context)
        mail.send_mail(subject, body, from_, [to, ])

    def save(self, commit=True):
        obj = super(InscriptionForm, self).save(commit=False)

        # Email de confirmação para o cliente
        self.send_mail(
            subject='Pré-Inscrição no Curso de Xadrez para Iniciantes realizada',
            from_=settings.DEFAULT_FROM_EMAIL,
            to=obj.email,
            template_name='courses/inscription_email.txt',
            context={'inscription': obj}
        )

        # Email para equipe ESTAVOS
        self.send_mail(
            subject='Nova inscrição do APRENDA recebida',
            from_=settings.DEFAULT_FROM_EMAIL,
            to='contato@estavos.com',
            template_name='courses/inscription_estavos_email.txt',
            context={'inscription': obj}
        )

        if commit:
            obj.save()

        return obj