# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from estavos.tournaments.views import TournamentDetail, InscriptionDetail, InscriptionControlView, \
    InscriptionControlConfirmView, DepositPaymentView
from estavos.tournaments.views import TournamentListView, InscriptionCreate, PaymentView


urlpatterns = [
    url(r'^$', TournamentListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', TournamentDetail.as_view(), name='detail'),
    url(r'^payment/(?P<slug>[a-f0-9]+)/$', PaymentView.as_view(), name='payment'),
    url(r'^payment/deposit/(?P<slug>[a-f0-9]+)/$', DepositPaymentView.as_view(), name='deposit_payment'),
    url(r'^(?P<tournament>[\d]+)/', include([
        url(r'^inscricoes/nova/$', InscriptionCreate.as_view(), name='inscription_new'),
        url(r'^inscricoes/(?P<slug>[a-f0-9]+)/$', InscriptionDetail.as_view(), name='inscription_detail'),
        url(r'^controle/inscricoes/$', InscriptionControlView.as_view(), name='inscriptions_control_list'),
        url(r'^controle/inscricoes/confirmar/(?P<pk>[\d]+)/$', InscriptionControlConfirmView.as_view(), name='inscriptions_control_confirm'),
    ])),
]
