# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import uuid
import logging
from braces.views import SuperuserRequiredMixin, FormValidMessageMixin
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView, TemplateView, RedirectView
from estavos.tournaments.forms import InscriptionForm, CompetitorFormSet
from itertools import groupby
from estavos.tournaments.models import Tournament, Inscription, Competitor, Payment, TournamentSchedule
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import SingleObjectMixin
from pagseguro.api import PagSeguroItem, PagSeguroApi
from django.http import HttpResponseServerError


class TournamentListView(ListView):
    model = Tournament
    queryset = Tournament.objects.all().filter(active=True)

    def get_context_data(self, **kwargs):
        kwargs = super(TournamentListView, self).get_context_data(**kwargs)
        inactive_tournaments = Tournament.objects.all().filter(active=False)
        kwargs['inactive_tournaments'] = inactive_tournaments
        return kwargs


class DepositPaymentView(SingleObjectMixin, TemplateView):
    model = Inscription
    template_name = 'payments/payment_done.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self._update_payment()
        return super().get(request, *args, **kwargs)

    def _update_payment(self):
        if not self.object.payment:
            payment = Payment.objects.create(
                paid=False,
                payment_type='2',
                status='1'
            )
            self.object.payment = payment
            self.object.save()


class PagsguroPaymentDone(TemplateView):
    template_name = 'payments/payment_done.html'

    def get(self, request, *args, **kwargs):
        pid = self.request.GET.get('pid')
        pagseguro_api = PagSeguroApi()
        data = pagseguro_api.get_transaction(pid)
        if data['success']:
            transaction = data['transaction']
            payment = Payment(
                status=transaction['status'],
                transaction=transaction['code']
            )
            if transaction['status'] in ['3', '4']:
                payment.paid = True
            payment.save()
            inscription = Inscription.objects.get(slug=transaction['reference'])
            inscription.payment = payment
            if payment.paid:
                inscription.confirmed = True
            inscription.save()
            kwargs['inscription'] = inscription
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)
        else:
            logging.error('Falha na página de retorno do pagamento')
            logging.error('Transação: {}'.format(pid))
            return HttpResponseServerError()


class PaymentView(SingleObjectMixin, RedirectView):
    model = Inscription

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        inscription = PagSeguroItem(
            id=self.object.pk,
            description='Incrição no torneio: {}'.format(self.object.tournament.title),
            quantity=self.object.competitors.all().count(),
            amount=self.object.tournament.price
        )
        pagseguro_api = PagSeguroApi(reference=self.object.slug)
        pagseguro_api.add_item(inscription)
        data = pagseguro_api.checkout()
        if not data['success']:
            logging.error('Falha ao processar pagamento')
            logging.error('ID da inscrição: {}'.format(self.object.slug))
            messages.error(
                self.request,
                'Houve um problema ao processar seu pagamento, ' \
                'entre em contato se o problema persistir'
            )
            return reverse('tournaments:list')
        return data['redirect_url']


class InscriptionCreate(SuccessMessageMixin, SingleObjectMixin, FormView):
    form_class = InscriptionForm
    template_name = 'tournaments/inscription_new.html'
    model = Tournament
    pk_url_kwarg = 'tournament'
    success_message = 'Inscrição realizada com sucesso.'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        # TODO: Check if tournament still has open inscriptions
        if not self.object.active:
            messages.info(request, 'O torneio que você tentou acessar não está ativo.')
            return redirect('tournaments:list')
        else:
            return super(InscriptionCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs = super(InscriptionCreate, self).get_context_data(**kwargs)
        if 'formset' not in kwargs:
            kwargs['formset'] = CompetitorFormSet()
        return kwargs

    def get_success_url(self):
        return reverse(
            'tournaments:inscription_detail',
            kwargs={'tournament': self.object.pk, 'slug': self.inscription_id}
        )

    def post(self, request, *args, **kwargs):
        formset = CompetitorFormSet(self.request.POST, self.request.FILES)
        form = self.get_form()
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form=form, formset=formset)
        else:
            return self.form_invalid(form=form, formset=formset)

    def form_valid(self, form, **kwargs):
        data_inscription = form.cleaned_data
        self.inscription_id = uuid.uuid4().hex
        inscription = Inscription.objects.create(
            tournament=self.object,
            name=data_inscription['name'],
            email=data_inscription['email'],
            phone=data_inscription['phone'],
            slug=self.inscription_id
        )
        competitors = kwargs['formset'].cleaned_data
        for competitor in competitors:
            if competitor:
                Competitor.objects.create(
                    name=competitor['name'],
                    birth=competitor['birth'],
                    id_lbx=competitor['id_lbx'],
                    id_fide=competitor['id_fide'],
                    club=competitor['club'],
                    inscription=inscription,
                )
        return super(InscriptionCreate, self).form_valid(form)

    def form_invalid(self, **kwargs):
        return self.render_to_response(
            self.get_context_data(form=kwargs['form'], formset=kwargs['formset'])
        )


class TournamentDetail(DetailView):
    model = Tournament

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schedules = TournamentSchedule.objects.filter(tournament=self.object).values('date', 'hour', 'activity')
        schedules = groupby(schedules, key=lambda s: s['date'])
        result = []
        for date, activities in schedules:
            result.append({
                'date': date,
                'activities': [{'hour': act['hour'], 'activity': act['activity']} for act in activities]
            })
        context['schedules'] = result
        return context


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

    def dispatch(self, request, *args, **kwargs):
        self.tournament = get_object_or_404(Tournament, pk=self.kwargs['tournament'], active=True)
        return super(InscriptionControlView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs = super(InscriptionControlView, self).get_context_data(**kwargs)
        kwargs['tournament'] = self.tournament
        kwargs['confirmed_inscriptions'] = Inscription.objects.filter(confirmed=True, tournament=self.tournament)
        return kwargs

    def get_queryset(self):
        return Inscription.objects.filter(confirmed=False, tournament=self.tournament)


class InscriptionControlConfirmView(SuperuserRequiredMixin, FormValidMessageMixin, TemplateView):
    template_name = 'tournaments/control/confirm_inscription.html'

    def dispatch(self, request, *args, **kwargs):
        self.tournament = get_object_or_404(Tournament, pk=self.kwargs['tournament'], active=True)
        self.inscription = get_object_or_404(Inscription, pk=self.kwargs['pk'], confirmed=False)
        return super(InscriptionControlConfirmView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs = super(InscriptionControlConfirmView, self).get_context_data(**kwargs)
        kwargs['tournament'] = self.tournament
        kwargs['inscription'] = self.inscription
        return kwargs

    def get_success_url(self):
        return reverse('tournaments:inscriptions_control_list', kwargs={'tournament': self.tournament.pk})

    def form_valid(self, form):
        self.inscription.confirmed = True
        self.inscription.save()
        form._send_mail(
            '{0}, Inscrição Confirmada! - {1}'.format(self.inscription.name, self.tournament),
            [self.inscription.email],
            'tournaments/control/inscription_confirmed_email.txt',
            {'inscription': self.inscription, 'tournament': self.tournament}
        )
        form._send_mail(
            'Inscrição {0} - {1}'.format(self.tournament, self.inscription.name),
            ['bruno@estavos.com', 'hugo@estavos.com'],
            'tournaments/control/arbiter_message_email.txt',
            {'inscription': self.inscription, 'tournament': self.tournament}
        )
        return super(InscriptionControlConfirmView, self).form_valid(form)

    def get_form_valid_message(self):
        return 'Inscrição do atleta {0} confirmada com sucesso.'.format(self.inscription.name)

