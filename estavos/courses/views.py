# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import resolve_url as r
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from estavos.courses.forms import InscriptionForm
from estavos.courses.models import Inscription, Course


class Home(TemplateView):
    template_name = 'courses/index.html'


class InscriptionView(CreateView):
    form_class = InscriptionForm
    model = Inscription

    def get_success_url(self):
        return r('courses:preinscription', self.object.pk)


class PreInscription(DetailView):
    template_name = 'courses/preinscription.html'
    model = Inscription


class CoursesListView(ListView):
    model = Course
    queryset = Course.objects.filter(is_active=True)
