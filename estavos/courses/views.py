# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import resolve_url as r
from django.views.generic import TemplateView, CreateView, DetailView
from estavos.courses.forms import InscriptionForm
from estavos.courses.models import Inscription


class Home(TemplateView):
    template_name = 'courses/index.html'


class InscriptionView(CreateView):
    template_name = 'courses/inscription_form.html'
    form_class = InscriptionForm
    model = Inscription

    def get_success_url(self):
        return r('courses:preinscription', self.object.pk)


class PreInscription(DetailView):
    template_name = 'courses/preinscription.html'
    model = Inscription
