# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from braces.views import SuperuserRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from estavos.tournaments.forms import InscriptionModelForm, InscriptionForm
from estavos.tournaments.models import Tournament, Inscription


class TournamentListView(ListView):
    model = Tournament
    queryset = Tournament.objects.all().filter(active=True)
    
    def get_context_data(self, **kwargs):
        kwargs = super(TournamentListView, self).get_context_data(**kwargs)
        inactive_tournaments = Tournament.objects.all().filter(active=False)
        kwargs['inactive_tournaments'] = inactive_tournaments
        return kwargs


class InscriptionCreate(CreateView):
    model = Inscription
    form_class = InscriptionModelForm
    template_name = 'tournaments/inscription_new.html'

    def dispatch(self, request, *args, **kwargs):
        tournament_id = self.kwargs['tournament']
        tournament = Tournament.objects.get(pk=tournament_id)
        if not tournament.active:
            messages.info(request, 'O torneio que você tentou acessar não está ativo.')
            return redirect('tournaments:list')
        else:
            return super(InscriptionCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs = super(InscriptionCreate, self).get_context_data(**kwargs)
        tournament_id = self.kwargs['tournament']
        tournament = Tournament.objects.get(pk=tournament_id)
        kwargs['tournament'] = tournament
        kwargs['object'] = tournament
        return kwargs

    def get_success_url(self):
        tournament = self.kwargs['tournament']
        return reverse(
            'tournaments:inscription_detail',
            kwargs={'tournament': tournament, 'slug': self.object.slug}
        )

    def form_valid(self, form):
        tournament = Tournament.objects.get(pk=self.kwargs['tournament'])
        form.instance.tournament = tournament
        form._send_mail(
            'Pré-inscrição: {0}'.format(form.instance.tournament),
            form.instance.email,
            'tournaments/inscription_email.txt',
            {'inscription': form.instance}
        )
        form._send_mail(
            'Nova inscrição: {0}'.format(form.instance.tournament),
            'torneios@estavos.com',
            'tournaments/inscription_admin_email.txt',
            {'inscription': form.instance}
        )
        return super(InscriptionCreate, self).form_valid(form)


class TournamentDetail(DetailView):
    model = Tournament

    def get_context_data(self, **kwargs):
        kwargs = super(TournamentDetail, self).get_context_data(**kwargs)
        kwargs['form'] = InscriptionForm()
        return kwargs


class InscriptionDetail(DetailView):
    model = Inscription
    template_name = 'tournaments/inscription_detail.html'

    def get_queryset(self):
        qs = super(InscriptionDetail, self).get_queryset()
        tournament = self.kwargs['tournament']
        qs = qs.filter(tournament=tournament)
        return qs


class InscriptionControlView(SuperuserRequiredMixin, ListView):
    model = Inscription
    template_name = 'tournaments/control/inscription_list.html'
    queryset = Inscription.objects.filter(confirmed=False)

    def get_context_data(self, **kwargs):
        kwargs = super(InscriptionControlView, self).get_context_data(**kwargs)
        tournament = get_object_or_404(Tournament, pk=self.kwargs['tournament'], active=True)
        kwargs['tournament'] = tournament
        return kwargs