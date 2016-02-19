# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import resolve_url as r
from django.views.generic import TemplateView, CreateView
from estavos.courses.forms import InscriptionForm
from estavos.courses.models import Inscription


class Home(TemplateView):
    template_name = 'courses/index.html'


class InscriptionView(CreateView):
    template_name = 'courses/inscription_form.html'
    form_class = InscriptionForm
    model = Inscription

    def get_success_url(self):
        return r('courses:preinscription')

    def form_valid(self, form):
        data = form.cleaned_data

        # Email de confirmação para o cliente
        form.send_mail(
            subject='Pré-Inscrição no Curso de Xadrez para Iniciantes realizada',
            from_=settings.DEFAULT_FROM_EMAIL,
            to=data['email'],
            template_name='courses/inscription_email.txt',
            context={'inscription': data}
        )

        # Email para equipe ESTAVOS
        form.send_mail(
            subject='Nova inscrição do APRENDA recebida',
            from_=settings.DEFAULT_FROM_EMAIL,
            to='contato@estavos.com',
            template_name='courses/inscription_estavos_email.txt',
            context={'inscription': data}
        )

        return super(InscriptionView, self).form_valid(form)


class PreInscription(TemplateView):
    template_name = 'courses/preinscription.html'
