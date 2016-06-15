# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from estavos.tournaments.views import TournamentDetail, InscriptionDetail, InscriptionControlView
from estavos.tournaments.views import TournamentListView, InscriptionCreate

urlpatterns = [
    url(r'^$', TournamentListView.as_view(), name='list'),
    # url(r'^(?P<pk>[\d]+)/$', TournamentDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/$', TournamentDetail.as_view(), name='detail'),
    url(r'^(?P<tournament>[\d]+)', include([
        url(r'^/inscricoes/nova/$', InscriptionCreate.as_view(), name='inscription_new'),
        url(r'^/inscricoes/(?P<slug>[a-f0-9]+)/$', InscriptionDetail.as_view(), name='inscription_detail'),
        url(r'^/controle/inscricoes/', InscriptionControlView.as_view(), name='inscriptions_control_list'),
    ])),
]
