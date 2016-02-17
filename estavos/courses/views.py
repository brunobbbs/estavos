# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from estavos.courses.forms import InscriptionForm


class Home(TemplateView):
    template_name = 'courses/index.html'


class Inscription(FormView):
    template_name = 'courses/inscription_form.html'
    form_class = InscriptionForm
    success_url = reverse_lazy('courses:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        places = dict(form.PLACES)
        classes = dict(form.KLASS)
        data.update({
            'place': places[data['place']],
            'klass': classes[data['klass']]
        })
        form.send_mail(
            subject='Pré-Inscrição no Curso de Xadrez para Iniciantes realizada',
            from_=settings.DEFAULT_FROM_EMAIL,
            to=data['email'],
            template_name='courses/inscription_email.txt',
            context={'inscription': data}
        )
        return super(Inscription, self).form_valid(form)


def thanks(request):
    return HttpResponse('ok')